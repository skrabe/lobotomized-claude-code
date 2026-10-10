<!--
name: 'Tool Result: hook error details hidden for URL secrets'
description: >-
  Note in a blocking hook failure explaining that error details are hidden
  because they may contain the hook URL's secrets.
ccVersion: 2.1.296
variables:
  - TOOL_RESULT_HOOK_ERROR_DETAILS_HIDDEN_URL_VAR_0
-->
Error details are hidden because they may contain this hook's URL, and any secrets in it can't be reliably removed. They will be shown if the URL starts with http:// or https:// and has no ${TOOL_RESULT_HOOK_ERROR_DETAILS_HIDDEN_URL_VAR_0}.
