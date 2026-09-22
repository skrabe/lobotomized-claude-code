<!--
name: 'Tool Description: WebFetch claude.ai artifact links exception'
description: >-
  WebFetch description bullet saying claude.ai artifact links are fetchable with
  the user's claude.ai login and to use WebFetch rather than curl or a headless
  browser for them
ccVersion: 2.1.277
-->
- Exception: claude.ai artifact links (claude.ai/artifact/{id} or claude.ai/code/artifact/{uuid}, including preview.claude.ai) ARE fetchable — WebFetch uses your claude.ai login. Use WebFetch for these, not curl or a headless browser (those return the SPA shell or a Cloudflare 403, not the content).
