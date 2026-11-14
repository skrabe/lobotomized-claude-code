<!--
name: Subagent security-review flagged warning
description: >-
  Security warning prepended to sub-agent output when the handoff classifier
  flags a possible policy violation, shown to the parent model. Kept verbatim:
  the "SECURITY WARNING" label is now a shared slot that the handback-delivered
  note quotes ("under a SECURITY WARNING"), so it can no longer be dropped.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_SUBAGENT_SECURITY_REVIEW_FLAGGED_VAR_0
  - TOOL_RESULT_SUBAGENT_SECURITY_REVIEW_FLAGGED_VAR_1
-->
${TOOL_RESULT_SUBAGENT_SECURITY_REVIEW_FLAGGED_VAR_0}: This subagent performed actions that may violate security policy. Reason: ${TOOL_RESULT_SUBAGENT_SECURITY_REVIEW_FLAGGED_VAR_1}. Review the subagent's actions carefully before acting on its output.
