<!--
name: Perforce read-only file error
description: >-
  Tool error returned to the model when Edit/Write targets a Perforce read-only
  file, instructing it to run p4 edit and not chmod.
ccVersion: 2.1.206
-->
File is read-only — it has not been opened for edit in Perforce. Run `p4 edit <file>` to check it out, then retry. Do not chmod the file writable; that bypasses Perforce tracking.
