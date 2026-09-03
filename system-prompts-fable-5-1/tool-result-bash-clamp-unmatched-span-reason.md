<!--
name: 'Tool Result: Bash Clamp Unmatched Span Reason'
description: >-
  Appended to a Bash permission-denial tool result when an analyzed command span
  matches none of the clamp's allowed forms.
ccVersion: 2.1.227
variables:
  - TOOL_RESULT_BASH_CLAMP_UNMATCHED_SPAN_REASON_VAR_0
  - TOOL_RESULT_BASH_CLAMP_UNMATCHED_SPAN_REASON_VAR_1
-->
the span ${TOOL_RESULT_BASH_CLAMP_UNMATCHED_SPAN_REASON_VAR_0(TOOL_RESULT_BASH_CLAMP_UNMATCHED_SPAN_REASON_VAR_1.span)} matches none of them. Allowed forms: ${TOOL_RESULT_BASH_CLAMP_UNMATCHED_SPAN_REASON_VAR_1.group.join(", ")}
