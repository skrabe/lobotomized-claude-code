<!--
name: 'Tool Parameter: Artifact DB replace_all'
description: >-
  `replace_all` on write_db str_replace: replace every occurrence of old_str
  instead of requiring exactly one.
ccVersion: 2.1.265
-->
write_db with db_op 'str_replace' only: replace every occurrence of old_str in the field instead of requiring it to occur exactly once (default false). old_str must still occur at least once.
