<!--
name: 'Tool result: Artifact db readback write without approval'
description: >-
  Artifact write_db error when a str_replace or if_version write has no approval
  record in this session.
ccVersion: 2.1.291
-->
this write reads back the stored document (a str_replace, or a write pinned with if_version) and has no approval record in this session — nothing was written; retry so it is checked again
