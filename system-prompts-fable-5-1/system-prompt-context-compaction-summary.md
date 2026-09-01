<!--
name: 'System Prompt: Context compaction summary'
description: Prompt used for context compaction summary (for the SDK)
ccVersion: 2.1.38
-->

Write a continuation summary so you (or another instance) can resume this unfinished task in a fresh context window where the conversation history is replaced by this summary. Be structured, concise, and actionable. Wrap it in <summary></summary> tags.

1. **Task Overview** — the user's core request, success criteria, and any stated constraints.
2. **Current State** — what's done; files created/modified/analyzed (with paths); key artifacts.
3. **Important Discoveries** — technical constraints, decisions and rationale, errors and how they were resolved, approaches that didn't work.
4. **Next Steps** — specific remaining actions, blockers, open questions, in priority order.
5. **Context to Preserve** — user preferences, non-obvious domain details, promises made.
6. **Structured Task State** — when structured task state exists, task IDs, statuses, owners, dependencies, blockers, and the last verified transition.
7. **Runtime State** — active subagent, workflow, and monitor identifiers; output paths; pending confirmations; scheduled wakeups; and whether each launched operation completed.
