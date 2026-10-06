<!--
name: PDF too-large note
description: >-
  Conditional note when a referenced PDF is too large for direct read. Empty .md
  body = silent omission.
ccVersion: 2.1.291
placeholders:
  - filename
  - page_count_text
  - file_size
  - read_tool
  - model_refused_note
shadows:
  - system-reminder-large-pdf-read-guidance
-->
PDF {{filename}}: {{page_count_text}}, {{file_size}}. Read via {{read_tool}} with `pages: "1-5"` (max 20/request; pages param required).
{{model_refused_note}}
