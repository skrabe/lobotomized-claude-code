<!--
name: 'Tool Description: Artifact Database if_version (App Wording)'
description: >-
  Person-worded database-description splice telling Claude to pass last-read
  version as if_version and redo on conflict.
ccVersion: 2.1.273
-->
 Claude passes the `version` it last read as `if_version` on every write to a document it has read ("batch" entries included), so that if someone has edited the document since, the write does nothing and names the current version, and Claude re-reads and redoes it instead of overwriting their change.
