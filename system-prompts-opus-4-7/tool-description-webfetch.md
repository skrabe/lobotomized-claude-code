<!--
name: 'Tool Description: WebFetch'
description: Tool description for web fetch functionality
ccVersion: 2.1.233
variables:
  - WEBFETCH_CACHE_TTL_FN
-->
Fetches a URL, converts HTML to markdown, processes it with a small fast model using your prompt, and returns the response.

- If an MCP web-fetch tool is available, prefer that — fewer restrictions.
- HTTP auto-upgrades to HTTPS.
- Read-only, no file modifications.
- Self-cleaning cache for repeated URLs (entries expire after ${WEBFETCH_CACHE_TTL_FN()}).
- On cross-host redirect, the tool reports the redirect URL — re-fetch it.
- For GitHub URLs, prefer `gh` via Bash (e.g. `gh pr view`, `gh api`).
- Fetch independent URLs in parallel — one message, multiple WebFetch calls.
