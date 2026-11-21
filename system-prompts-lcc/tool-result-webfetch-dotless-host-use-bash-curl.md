<!--
name: 'Tool Result: WebFetch dotless host, use Bash curl'
description: >-
  WebFetch error thrown for localhost or dotless hostnames, with an optional
  hint to use Bash with curl.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_WEBFETCH_DOTLESS_HOST_USE_BASH_CURL_VAR_0
-->
WebFetch cannot fetch localhost or other hostnames without a dot.${TOOL_RESULT_WEBFETCH_DOTLESS_HOST_USE_BASH_CURL_VAR_0()?"":" To reach a local server, use Bash with curl instead."}
