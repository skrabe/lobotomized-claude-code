<!--
name: 'Tool Description: WebSearch (concise)'
description: >-
  Concise (velvet) WebSearch tool description rendered for Opus 4.8 / Fable 5 /
  Mythos 5 — US-only web search returning titled URL result blocks, with the
  current-month grounding note
ccVersion: 2.1.295
variables:
  - CURRENT_MONTH_YEAR
  - IS_WEBSEARCH_CITATIONS_ENABLED
  - UNTRUSTED_SEARCH_RESULT_CONTENT_NOTE
-->
Search the web. Returns result blocks with titles and URLs. US-only.

- The current month is ${CURRENT_MONTH_YEAR} — use this when searching for recent information.
- \`allowed_domains\` / \`blocked_domains\` filter results.
- ${IS_WEBSEARCH_CITATIONS_ENABLED?UNTRUSTED_SEARCH_RESULT_CONTENT_NOTE:'After answering from results, end with a "Sources:" list of the URLs you used as markdown links.'}
