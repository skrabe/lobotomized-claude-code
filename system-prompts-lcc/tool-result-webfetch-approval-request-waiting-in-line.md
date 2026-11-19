<!--
name: 'Tool Result: WebFetch approval request waiting in line'
description: >-
  WebFetch result when a URL was not fetched because an earlier permission
  request was still waiting for the user's answer
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_WEBFETCH_APPROVAL_REQUEST_WAITING_IN_LINE_VAR_0
  - TOOL_RESULT_WEBFETCH_APPROVAL_REQUEST_WAITING_IN_LINE_VAR_1
-->
${TOOL_RESULT_WEBFETCH_APPROVAL_REQUEST_WAITING_IN_LINE_VAR_0.url} was not fetched: the request to approve it was not sent to the user, because an earlier permission request was still waiting for their answer. Once no request is waiting for them, a new ${TOOL_RESULT_WEBFETCH_APPROVAL_REQUEST_WAITING_IN_LINE_VAR_1.tool.name} call with this URL fetches the page if the URL is allowed by then, and otherwise sends them a new request.
