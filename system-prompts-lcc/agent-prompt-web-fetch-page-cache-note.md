<!--
name: 'Agent Prompt: Web fetch page cache note'
description: >-
  Note in the web-fetch agent's when-to-use text that pages are cached per URL
  for a period, so a repeat fetch returns the same copy
ccVersion: 2.1.328
variables:
  - AGENT_PROMPT_WEB_FETCH_PAGE_CACHE_NOTE_VAR_0
-->
 Pages are cached for ${AGENT_PROMPT_WEB_FETCH_PAGE_CACHE_NOTE_VAR_0()} per URL, so a repeat fetch in that time returns the same copy.
