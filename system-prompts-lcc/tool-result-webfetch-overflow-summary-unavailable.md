<!--
name: 'Tool Result: WebFetch overflow summary unavailable'
description: >-
  Appended to the WebFetch page result when the secondary summarizer call for
  the truncated remainder failed, telling the model that part of the page is
  unknown to it.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_WEBFETCH_OVERFLOW_SUMMARY_UNAVAILABLE_VAR_0
  - TOOL_RESULT_WEBFETCH_OVERFLOW_SUMMARY_UNAVAILABLE_VAR_1
  - TOOL_RESULT_WEBFETCH_OVERFLOW_SUMMARY_UNAVAILABLE_VAR_2
-->


${TOOL_RESULT_WEBFETCH_OVERFLOW_SUMMARY_UNAVAILABLE_VAR_0} The remaining ${TOOL_RESULT_WEBFETCH_OVERFLOW_SUMMARY_UNAVAILABLE_VAR_1.length} characters were NOT read: the secondary model call that would have summarized them did not complete. ${TOOL_RESULT_WEBFETCH_OVERFLOW_SUMMARY_UNAVAILABLE_VAR_2?"Unless you go on to read them, say":"Say"} in your report that this part of the page is unknown to you.]
