<!--
name: 'Security review: final reply with closing lines'
description: >-
  Variant closing of the /security-review prompt requiring the report followed
  by host-supplied closing lines verbatim.
ccVersion: 2.1.318
variables:
  - SYSTEM_PROMPT_SECURITY_REVIEW_FINAL_REPLY_CLOSING_LINES_VAR_0
-->
Your final reply must contain the markdown report, then these two lines exactly as written, and nothing else:
${SYSTEM_PROMPT_SECURITY_REVIEW_FINAL_REPLY_CLOSING_LINES_VAR_0.join(`
`)}
