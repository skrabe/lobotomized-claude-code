<!--
name: 'Tool Result: Git Bundle Reftable Refs'
description: >-
  Refuses the upload when the repository stores refs in reftable format, which
  the upload cannot yet vouch for table by table.
ccVersion: 2.1.246
-->
Not uploading this working tree: this repository keeps its refs in the reftable format, whose tables the upload cannot yet vouch for one by one. Start from a clone made with the default (files) ref format instead.
