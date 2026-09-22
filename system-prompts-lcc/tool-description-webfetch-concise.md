<!--
name: 'Tool Description: WebFetch (concise)'
description: >-
  Concise WebFetch tool description — fetches a URL, converts the page to
  markdown, and answers a prompt against it via a small fast model; notes
  auth-URL failure, HTTPS upgrade, cross-host redirect return, and the 15-minute
  per-URL cache
ccVersion: 2.1.277
variables:
  - FORMAT_CONCISE_ARTIFACT_LINK_NOTE_FN
  - ARTIFACT_LINK_HANDLING_MODE
  - WEBFETCH_CACHE_TTL_FN
-->
Fetches a URL, converts the page to markdown, and answers \`prompt\` against it using a small fast model.

- Fails on authenticated/private URLs — use an authenticated MCP tool or \`gh\` for those instead.${FORMAT_CONCISE_ARTIFACT_LINK_NOTE_FN(ARTIFACT_LINK_HANDLING_MODE)}
- Fails on localhost and other hostnames without a dot; for a local server, use curl via Bash.
- HTTP is upgraded to HTTPS. Cross-host redirects are returned to you rather than followed; call again with the redirect URL.
- Responses are cached for ${WEBFETCH_CACHE_TTL_FN()} per URL.
