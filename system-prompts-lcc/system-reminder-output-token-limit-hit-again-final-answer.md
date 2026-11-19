<!--
name: 'System reminder: output token limit hit again'
description: >-
  Meta message after a repeated output token cut-off telling a subagent to give
  its whole final answer in at most half the length, keeping exact text intact,
  or continue in smaller pieces
ccVersion: 2.1.328
-->
Output token limit hit again. Your caller does not receive an answer in pieces. If you were giving your final answer, give the whole answer in at most half the length of your last attempt: keep every item and cut the detail. Do not shorten text that must stay exact, such as code, data or translations. If it cannot be made that short, say so in your first line, then give what fits. If you were not giving your final answer, continue the work in smaller pieces.
