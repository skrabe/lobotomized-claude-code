<!--
name: 'Tool Result: Grep ripgrep target unreadable retry guidance'
description: >-
  Guidance appended when ripgrep could not read its target for a non-permission
  reason: retry once, then tell the user, and do not fall back to a shell
  recursive search
ccVersion: 2.1.292
variables:
  - TOOL_RESULT_GREP_RIPGREP_TARGET_UNREADABLE_RETRY_GUIDANCE_VAR_0
-->
Run the search once more. If it fails again, tell the user that the search is failing. ${TOOL_RESULT_GREP_RIPGREP_TARGET_UNREADABLE_RETRY_GUIDANCE_VAR_0}: it can also reach other files, which this tool is set to leave out.
