<!--
name: 'Tool Result: Skill unknown, did you mean claude.ai account skill'
description: >-
  Skill tool validation error returned when an unknown skill name resolves to a
  skill synced from the user's claude.ai account under a former namespace,
  naming it and telling the model to invoke it by its full name
ccVersion: 2.1.282
variables:
  - TOOL_RESULT_SKILL_UNKNOWN_DID_YOU_MEAN_CLAUDE_AI_ACCOUNT_SKILL_VAR_0
  - TOOL_RESULT_SKILL_UNKNOWN_DID_YOU_MEAN_CLAUDE_AI_ACCOUNT_SKILL_VAR_1
-->
Unknown skill: ${TOOL_RESULT_SKILL_UNKNOWN_DID_YOU_MEAN_CLAUDE_AI_ACCOUNT_SKILL_VAR_0}. Did you mean ${TOOL_RESULT_SKILL_UNKNOWN_DID_YOU_MEAN_CLAUDE_AI_ACCOUNT_SKILL_VAR_1.name} (a skill from the user's claude.ai account, not one Anthropic publishes)? Invoke it by that full name.
