<!--
name: 'Data: Managed Agents client patterns'
description: >-
  Reference guide of common client-side patterns for driving Managed Agent
  sessions, including stream reconnection, idle-break gating, tool
  confirmations, interrupts, and custom tools
ccVersion: 2.1.237
-->

# Managed Agents — client patterns

Robust clients stream events, persist processed event IDs, reconnect after drops, and treat `idle`/`terminated` as separate gates. Send interrupts and tool confirmations through the session APIs, not ad-hoc side channels.

- `requires_action` — agent is waiting on a client-side event (tool confirmation, custom tool result). Handle it, don't break. **Self-hosted exception:** if the session went `requires_action`-idle with no pending `agent.tool_use` (always_ask) or `agent.custom_tool_use` to answer, the worker failed the claimed work item (typically a memory-store mount error, logged only on the worker host). Don't `continue` forever on that — surface it, fix the host, and send `user.interrupt` to re-queue the work (`shared/managed-agents-self-hosted-sandboxes.md` § Memory stores → Troubleshooting).

For custom tools, keep secrets on the host side and return only the result the agent needs. Fetch current docs for precise event ordering and SDK method names.
