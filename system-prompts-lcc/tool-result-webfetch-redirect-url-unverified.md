<!--
name: WebFetch redirect URL unverified
description: >-
  Redirect result line relaying the server-supplied Location target with
  withheld-length and hostname-length caveats.
ccVersion: 2.1.232
variables:
  - TOOL_RESULT_WEBFETCH_REDIRECT_URL_UNVERIFIED_VAR_0
  - TOOL_RESULT_WEBFETCH_REDIRECT_URL_UNVERIFIED_VAR_1
  - TOOL_RESULT_WEBFETCH_REDIRECT_URL_UNVERIFIED_VAR_2
  - TOOL_RESULT_WEBFETCH_REDIRECT_URL_UNVERIFIED_VAR_3
-->
Redirect URL (from the server's Location header — server-supplied, not verified): ${TOOL_RESULT_WEBFETCH_REDIRECT_URL_UNVERIFIED_VAR_0}${TOOL_RESULT_WEBFETCH_REDIRECT_URL_UNVERIFIED_VAR_1>0?` […${TOOL_RESULT_WEBFETCH_REDIRECT_URL_UNVERIFIED_VAR_1} more characters withheld: too long to relay]`:""}${TOOL_RESULT_WEBFETCH_REDIRECT_URL_UNVERIFIED_VAR_2?` [hostname longer than any DNS name (${TOOL_RESULT_WEBFETCH_REDIRECT_URL_UNVERIFIED_VAR_3} characters): not a fetchable address]`:""}
