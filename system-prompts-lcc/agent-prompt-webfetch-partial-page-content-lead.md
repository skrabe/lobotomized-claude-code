<!--
name: 'Agent Prompt: WebFetch partial page content lead'
description: >-
  Lead line for the WebFetch extraction model saying the content is one part of
  a longer page starting at the given offset
ccVersion: 2.1.291
variables:
  - AGENT_PROMPT_WEBFETCH_PARTIAL_PAGE_CONTENT_LEAD_VAR_0
  - AGENT_PROMPT_WEBFETCH_PARTIAL_PAGE_CONTENT_LEAD_VAR_1
-->
The content below is one part of a longer page: it starts ${AGENT_PROMPT_WEBFETCH_PARTIAL_PAGE_CONTENT_LEAD_VAR_0} characters into the page's ${AGENT_PROMPT_WEBFETCH_PARTIAL_PAGE_CONTENT_LEAD_VAR_1.length}.
