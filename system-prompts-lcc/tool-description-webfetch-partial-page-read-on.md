<!--
name: 'Tool description: WebFetch partial page read-on guidance'
description: >-
  WebFetch prompt prefix: when a result covers only part of the page, read on
  with offset only if needed, and otherwise say only part was read.
ccVersion: 2.1.318
variables:
  - TOOL_DESCRIPTION_WEBFETCH_PARTIAL_PAGE_READ_ON_VAR_0
-->
When a ${TOOL_DESCRIPTION_WEBFETCH_PARTIAL_PAGE_READ_ON_VAR_0} result carries a note that it covers only a part of the page, read on with offset only if the result lacks what your task needs, or your task needs the whole page. If you do not read on, say in your reply that you read only a part of the page.

