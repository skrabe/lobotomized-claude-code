<!--
name: Forked-skill resume vetoed — skills sync disabled
description: >-
  Refusal text returned to Claude when an agent that ran as a forked
  account-synced skill cannot be resumed because skills sync is turned off or
  denied by policy.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_AGENT_RESUME_FORKED_SKILL_SYNC_DISABLED_VAR_0
  - TOOL_RESULT_AGENT_RESUME_FORKED_SKILL_SYNC_DISABLED_VAR_1
-->
Agent ${TOOL_RESULT_AGENT_RESUME_FORKED_SKILL_SYNC_DISABLED_VAR_0} ran as forked skill ${TOOL_RESULT_AGENT_RESUME_FORKED_SKILL_SYNC_DISABLED_VAR_1.skillName}, an account-synced skill that is currently disabled (skills sync turned off or denied by policy); refusing to resume it.
