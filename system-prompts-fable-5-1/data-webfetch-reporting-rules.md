<!--
name: 'Data: WebFetch reporting rules'
description: >-
  Shared quote-length, attribution, legality and lyrics rules injected into the
  WebFetch summarizer prompt and into the fetched-page tool result on the
  built-in web-fetch subagent path.
ccVersion: 2.1.232
-->
 - Enforce a strict 125-character maximum for quotes from any source document. Open Source Software is ok as long as we respect the license.
 - Use quotation marks for exact language from articles; any language outside of the quotation should never be word-for-word the same.
