<!--
name: 'Tool result: agent not resumed, no typed app message'
description: >-
  Refusal: a user-stopped agent resumes only in answer to a message the user
  typed in the Claude app after the Stop.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_AGENT_NOT_RESUMED_NOT_TYPED_IN_APP_VAR_0
-->
Agent ${TOOL_RESULT_AGENT_NOT_RESUMED_NOT_TYPED_IN_APP_VAR_0} ended when the user pressed Stop, and was not resumed. It can be resumed only in answer to a message that the user types in the Claude app (web, desktop or mobile) after the Stop. This turn answers no such message, so its work stays stopped until the user asks for it there.
