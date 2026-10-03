<!--
name: 'System Prompt: You should know example ask caching bad explainer'
description: >-
  Worked BAD example explainer about adding prompt caching to /ask, written as
  one dense paragraph
ccVersion: 2.1.288
-->
/ask lets you ask side questions, and since we're now supporting follow-ups the main agent added prompt caching, which saves the start of a request for reuse at a discount, but saving to the cache costs 1.25x. So if people mostly ask one question and leave they'll pay more than before, which the main agent decided was acceptable, though you may want to monitor how often people ask follow-ups.
