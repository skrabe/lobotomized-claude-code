<!--
name: 'Tool Result: Remote Tool Person Approval Required'
description: >-
  Remote-tool error when automatic approval is insufficient because only a
  person's approval counts, so the call did not run.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_REMOTE_TOOL_PERSON_APPROVAL_REQUIRED_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_PERSON_APPROVAL_REQUIRED_VAR_1
-->
This session's automatic check approved this ${TOOL_RESULT_REMOTE_TOOL_PERSON_APPROVAL_REQUIRED_VAR_0} call, but for ${TOOL_RESULT_REMOTE_TOOL_PERSON_APPROVAL_REQUIRED_VAR_0} on ${TOOL_RESULT_REMOTE_TOOL_PERSON_APPROVAL_REQUIRED_VAR_1} only a person's approval counts in this session, so it was not cleared to run and nothing ran. Send the call again and ask the user to approve it from the terminal or desktop prompt.
