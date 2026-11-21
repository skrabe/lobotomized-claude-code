<!--
name: 'Tool Result: WebFetch partial page content lead'
description: >-
  Lead line of WebFetch content noting the content is one part of a longer page
  starting at the given character offset.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_WEBFETCH_PARTIAL_PAGE_CONTENT_LEAD_VAR_0
  - TOOL_RESULT_WEBFETCH_PARTIAL_PAGE_CONTENT_LEAD_VAR_1
  - TOOL_RESULT_WEBFETCH_PARTIAL_PAGE_CONTENT_LEAD_VAR_2
  - TOOL_RESULT_WEBFETCH_PARTIAL_PAGE_CONTENT_LEAD_VAR_3
-->
${TOOL_RESULT_WEBFETCH_PARTIAL_PAGE_CONTENT_LEAD_VAR_0?.TOOL_RESULT_WEBFETCH_PARTIAL_PAGE_CONTENT_LEAD_VAR_1??""}${TOOL_RESULT_WEBFETCH_PARTIAL_PAGE_CONTENT_LEAD_VAR_2>0?`The content below is one part of a longer page: it starts ${TOOL_RESULT_WEBFETCH_PARTIAL_PAGE_CONTENT_LEAD_VAR_2} characters into the page's ${TOOL_RESULT_WEBFETCH_PARTIAL_PAGE_CONTENT_LEAD_VAR_3.length}.
`:""}
