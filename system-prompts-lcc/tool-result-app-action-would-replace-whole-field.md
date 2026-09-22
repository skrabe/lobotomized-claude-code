<!--
name: 'Tool Result: App Action Would Replace Whole Field'
description: >-
  would_replace_content reason: positional insert failed and replacing the whole
  non-empty field needs overwrite_existing: true.
ccVersion: 2.1.246
-->
positional insert (set AXSelectedText) didn't take here, and the only fallback is replacing the WHOLE field's content (set AXValue), but the field is not empty. To proceed, retry app_type with overwrite_existing: true
