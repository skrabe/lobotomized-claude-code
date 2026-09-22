<!--
name: 'Tool Description: Artifact Database str_replace'
description: >-
  Artifact-database tool-description clause explaining in-place str_replace on a
  string field and when to prefer it over resending the field.
ccVersion: 2.1.265
-->
 "str_replace" changes text inside one string field in place (`collection`, `doc_id`, `field`, `old_str`, `new_str`; old_str must occur exactly once in the field, or nothing is written — or pass `replace_all: true` to change every occurrence) — prefer it to resending a large field for a small edit,
