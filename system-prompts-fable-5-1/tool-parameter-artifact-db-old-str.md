<!--
name: 'Tool Parameter: Artifact DB old_str'
description: >-
  `old_str` on write_db str_replace: the exact text to replace, which must occur
  once unless replace_all is set.
ccVersion: 2.1.265
-->
write_db with db_op 'str_replace' only: the exact text to replace, as it appears in the field's value. It must occur exactly once in that field; otherwise nothing is written and the result says whether it was absent or not unique.
