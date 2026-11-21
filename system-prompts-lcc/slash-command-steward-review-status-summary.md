<!--
name: 'Slash Command: Steward review status summary'
description: >-
  Summarizes Claude's newest review comment head and which commits the hosted
  review reported on
ccVersion: 2.1.330
variables:
  - SLASH_COMMAND_STEWARD_REVIEW_STATUS_SUMMARY_VAR_0
  - SLASH_COMMAND_STEWARD_REVIEW_STATUS_SUMMARY_VAR_1
-->
${SLASH_COMMAND_STEWARD_REVIEW_STATUS_SUMMARY_VAR_0===void 0?"You have posted no review comment on it yet.":`Your newest review comment on it names the head ${SLASH_COMMAND_STEWARD_REVIEW_STATUS_SUMMARY_VAR_0}.`} ${SLASH_COMMAND_STEWARD_REVIEW_STATUS_SUMMARY_VAR_1.length===0?"Claude's hosted review has reported on no commit of it.":`Claude's hosted review has reported on: ${SLASH_COMMAND_STEWARD_REVIEW_STATUS_SUMMARY_VAR_1.join(", ")}.`}
