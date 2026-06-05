# Azure OpenAI GPT-5.x transport routing

A practical operations note for running Azure OpenAI GPT-5.x deployments behind local-first AI agents and automation systems.

The core lesson: do not rely on model-name guessing or SDK defaults when a deployment can be called through more than one API surface. Pin the transport explicitly per deployment and per task.

## Problem

Azure OpenAI GPT-5.x deployments can appear confusing because the portal, SDKs, and runtime endpoints may use overlapping terms:

- a deployment can be created from a model that is shown in a chat-oriented surface;
- the same deployment name can be used with the Responses API;
- some clients still assume Chat Completions payloads for GPT-5.x models;
- some SDK integrations route to `/chat/completions` even when the model or endpoint expects `/responses`.

A common failure mode is sending a Chat Completions payload to a Responses API route.

Typical error:

```text
Unsupported parameter: 'messages'. In the Responses API, this parameter has moved to 'input'.
```

The inverse can also happen: a client tries a Responses URL shape that is not supported by the selected endpoint variant or drops a required path/query component, producing `404 Resource not found`.

## Why this matters for agents

Agent systems often use multiple model calls in one user-visible turn:

- main reasoning or chat model;
- coding/delegation model;
- summarization model;
- web extraction model;
- memory/session-search model;
- compression model.

If transport selection is implicit, one auxiliary call can fail or retry for a long time even when the main model is healthy. The user experiences this as random latency, broken streams, or delayed answers.

## Recommended pattern

Use explicit routing per task, not one global assumption.

Example operational policy:

```yaml
main_chat_model:
  api_surface: chat_completions
  purpose: primary assistant conversation

coding_model:
  api_surface: chat_completions
  purpose: coding and code review workflows

auxiliary_summary_model:
  api_surface: responses
  purpose: compression, search summarization, and extraction summaries
```

This is intentionally conceptual. Use the configuration names required by your framework. For example, one agent framework may call the Responses wrapper `responses`, another may call it `openai_responses`, and another may use a provider-specific alias.

## Diagnostic checklist

When Azure GPT-5.x calls fail, check these before changing models:

1. **Endpoint family**
   - Is the base URL the newer `/openai/v1/` form?
   - Or is it the older deployment/API-version form?
   - Is it an Azure OpenAI hostname or a Cognitive Services hostname?

2. **Payload shape**
   - Chat Completions expects `messages`.
   - Responses expects `input`.

3. **Client route**
   - Chat Completions route: `/chat/completions`.
   - Responses route: `/responses`.

4. **Deployment name**
   - Use the deployment name assigned in Azure, not necessarily the model catalog name.

5. **SDK behavior**
   - Some SDKs or wrappers choose routes based on model-name heuristics.
   - Heuristics can lag behind newly released GPT-5.x variants.
   - Prefer explicit configuration over automatic detection.

6. **Error signature**
   - `Unsupported parameter: 'messages'` usually means a Chat Completions payload reached a Responses API path.
   - `Resource not found` can mean wrong path, wrong endpoint variant, missing API version on legacy endpoints, or wrong deployment name.
   - Long pauses after the first byte can be a streaming/SSE issue and should be debugged separately from transport mismatch.

## Minimal smoke tests

Run small direct calls before blaming agent logic.

### Chat Completions shape

```bash
curl -sS "$AZURE_OPENAI_BASE_URL/chat/completions" \
  -H "Content-Type: application/json" \
  -H "api-key: $AZURE_OPENAI_API_KEY" \
  -d '{
    "model": "YOUR_DEPLOYMENT_NAME",
    "messages": [{"role": "user", "content": "Reply with ok."}],
    "max_completion_tokens": 20
  }'
```

### Responses shape

```bash
curl -sS "$AZURE_OPENAI_BASE_URL/responses" \
  -H "Content-Type: application/json" \
  -H "api-key: $AZURE_OPENAI_API_KEY" \
  -d '{
    "model": "YOUR_DEPLOYMENT_NAME",
    "input": "Reply with ok.",
    "max_output_tokens": 20
  }'
```

Use placeholder deployment names in public docs. Never publish real endpoints, keys, tenant IDs, internal resource names, logs, or customer context.

## Agent configuration guidance

For production-like local agents:

- Keep the main chat deployment on the API surface it is known to support reliably.
- Keep coding/delegation deployments explicitly pinned instead of inheriting defaults.
- Route lightweight summarization, compression, and retrieval helpers through the API surface that their deployment actually accepts.
- Disable or reduce fallback/model-hopping when debugging transport issues; retries against the wrong API only add latency.
- Log provider, model/deployment, base URL family, API surface, and error class, but redact keys and private resource names.

## Public-safe incident note template

```markdown
## Incident

A GPT-5.x auxiliary call failed because the client sent a Chat Completions-style payload to a Responses API route.

## Symptom

`Unsupported parameter: 'messages'. In the Responses API, this parameter has moved to 'input'.`

## Fix

Pinned API transport per task:

- main chat: Chat Completions
- coding/delegation: Chat Completions
- auxiliary summarization/compression: Responses

## Follow-up

Added smoke tests for both route shapes and documented expected error signatures.
```

## References

- Microsoft Learn: Azure OpenAI v1 API uses the standard OpenAI client and `/openai/v1/` base URL.
- Microsoft Learn: Azure OpenAI Responses API documentation.
- Microsoft Q&A: GPT-5 Responses API is a protocol layer; there is no separate Responses deployment toggle.
- GitHub discussions and issues from multiple clients show the same operational failure mode: GPT-5.x integrations need explicit routing between Chat Completions and Responses.

## Takeaway

For Azure OpenAI GPT-5.x agents, transport routing is an operations concern. Treat it like any other runtime contract: make it explicit, test it directly, and keep private deployment details out of public documentation.
