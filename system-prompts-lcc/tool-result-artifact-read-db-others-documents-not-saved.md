<!--
name: 'Tool result: artifact read_db others'' documents not saved'
description: >-
  Deny message when read_db out_dir would save documents others may have
  written; nothing saved, omit out_dir or ask the user first.
ccVersion: 2.1.318
-->
Documents that other people may have written are not saved to files, because a file drops the note that marks them as others' — nothing was saved. Omit out_dir to read them into the conversation; if the user wants them as files, tell the user that first and ask.
