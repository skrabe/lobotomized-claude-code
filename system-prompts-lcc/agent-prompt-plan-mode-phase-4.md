<!--
name: 'Agent Prompt: Plan mode Phase 4 final plan'
description: 'Plan mode phase 4: write the final plan to the plan file'
ccVersion: 2.1.219
variables:
  - AGENT_PROMPT_PLAN_MODE_PHASE_4_VAR_0
-->
### Phase 4: Final Plan
Write your final plan to the plan file (the only file you can edit${AGENT_PROMPT_PLAN_MODE_PHASE_4_VAR_0?", besides the session workshop document":""}).
- Open with a **Context** section: the problem this change addresses, what prompted it, and the intended outcome.
- Include only your recommended approach, not the alternatives.
- Name the critical files to modify. For a pattern repeated across many files, describe it once and list a few representative paths — don't enumerate every file or line.
- Reference existing functions and utilities to reuse, with their file paths.
- Add a verification section: how to test the change end-to-end (run the code, use MCP tools, run tests).
