<!--
name: 'Tool Parameter: Artifact Action str_replace'
description: >-
  Action-enum clause describing db_op str_replace (and if_version on
  update/str_replace) spliced into the read_db/write_db description when that op
  is enabled.
ccVersion: 2.1.265
-->
 'str_replace' with `collection`, `doc_id`, `field`, `old_str`, `new_str` swaps one exact, unique piece of text inside a string field without resending it (`replace_all`: every occurrence); 'update' and 'str_replace' take `if_version` (the document's last-read `version`) and write nothing if it has changed since;
