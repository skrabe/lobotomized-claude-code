<!--
name: 'Tool result: WebFetch domain check rate-limited'
description: >-
  WebFetch error when the domain safety check is rate-limited: do not retry in a
  loop or sleep, continue without the page and report it; one later attempt is
  fine.
ccVersion: 2.1.286
variables:
  - TOOL_RESULT_WEBFETCH_DOMAIN_CHECK_RATE_LIMITED_VAR_0
  - TOOL_RESULT_WEBFETCH_DOMAIN_CHECK_RATE_LIMITED_VAR_1
-->
The safety check for domain ${TOOL_RESULT_WEBFETCH_DOMAIN_CHECK_RATE_LIMITED_VAR_0} is rate-limited (too many domain checks from this network; the limit is shared and can stay exhausted for minutes). Do not retry ${TOOL_RESULT_WEBFETCH_DOMAIN_CHECK_RATE_LIMITED_VAR_1} in a loop or sleep to wait it out; continue without this page and report that its safety check was rate-limited. A single later attempt is fine; if that is rate-limited too, stop.
