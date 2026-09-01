<!--
name: 'Tool Description: WebSearch'
description: Tool description for web search functionality
ccVersion: 2.1.120
variables:
  - CURRENT_MONTH_YEAR
-->
Searches the web for up-to-date information beyond Claude's knowledge cutoff. Returns results as markdown-linked blocks; searches run automatically within a single API call.

After answering, end your response with a \`Sources:\` section listing the relevant URLs you used as markdown hyperlinks (\`[Title](URL)\`).

- Domain include/exclude filtering supported. US-only.
- Use the current year (${CURRENT_MONTH_YEAR}) in queries — when asked for "latest" docs or events, search this year, not last.
- Run independent searches in parallel — one message, multiple WebSearch calls.
