<!--
name: 'Tool Result: Full PDF read unsupported on model'
description: >-
  Read tool error when the current model cannot read whole PDFs: use a newer
  model or the pages parameter, with poppler-utils install hints.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_PDF_FULL_READ_UNSUPPORTED_MODEL_VAR_0
-->
Reading full PDFs is not supported with this model. Use a newer model (Sonnet 3.5 v2 or later), or use the pages parameter to read specific page ranges (e.g., pages: "1-5", maximum ${TOOL_RESULT_PDF_FULL_READ_UNSUPPORTED_MODEL_VAR_0} pages per request). Page extraction requires poppler-utils: install with \`brew install poppler\` on macOS or \`apt-get install poppler-utils\` on Debian/Ubuntu.
