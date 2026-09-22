<!--
name: Artifact Auto-Open After First Write
description: >-
  validateInput refusal when auto_open is after_first_write on a type_url
  create, which is already the first write.
ccVersion: 2.1.247
-->
`auto_open`: "after_first_write" has nothing to wait for — this call's `file_path` publish is its first write; remove `auto_open`
