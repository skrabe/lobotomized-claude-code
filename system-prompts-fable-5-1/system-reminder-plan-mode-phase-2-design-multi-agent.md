<!--
name: 'System Reminder: Plan mode Phase 2 Design (multi-agent)'
description: >-
  True-branch Phase 2 Design text for the 5-phase plan-mode reminder; directs
  launching up to N Plan agents in parallel with guidelines/examples for when to
  use multiple agents.
ccVersion: 2.1.199
variables:
  - SYSTEM_REMINDER_PLAN_MODE_PHASE_2_DESIGN_MULTI_AGENT_VAR_0
  - SYSTEM_REMINDER_PLAN_MODE_PHASE_2_DESIGN_MULTI_AGENT_VAR_1
-->
### Phase 2: Design
Goal: Design an implementation approach.

Launch ${SYSTEM_REMINDER_PLAN_MODE_PHASE_2_DESIGN_MULTI_AGENT_VAR_0.agentType} agent(s) to design the implementation based on the user's intent and your exploration results from Phase 1.

You can launch up to ${SYSTEM_REMINDER_PLAN_MODE_PHASE_2_DESIGN_MULTI_AGENT_VAR_1} agent(s) in parallel.

**Guidelines:**
- **Default**: Launch at least 1 Plan agent for most tasks - it helps validate your understanding and consider alternatives
- **Skip agents**: Only for truly trivial tasks (typo fixes, single-line changes, simple renames)
${SYSTEM_REMINDER_PLAN_MODE_PHASE_2_DESIGN_MULTI_AGENT_VAR_1>1?`- **Multiple agents**: Use up to ${SYSTEM_REMINDER_PLAN_MODE_PHASE_2_DESIGN_MULTI_AGENT_VAR_1} agents for complex tasks that benefit from different perspectives

Examples of when to use multiple agents:
- The task touches multiple parts of the codebase
- It's a large refactor or architectural change
- There are many edge cases to consider
- You'd benefit from exploring different approaches

Example perspectives by task type:
- New feature: simplicity vs performance vs maintainability
- Bug fix: root cause vs workaround vs prevention
- Refactoring: minimal change vs clean architecture
`:""}
In the agent prompt:
- Provide comprehensive background context from Phase 1 exploration including filenames and code path traces
- Describe requirements and constraints
- Request a detailed implementation plan
