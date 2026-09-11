<!--
name: Artifact Read Db Out Dir No Consent Surface
description: >-
  checkPermissions deny for read_db out_dir outside working folders when no live
  consent surface exists.
ccVersion: 2.1.268
-->
read_db saves outside this session’s working folders only with the user’s approval, and no one can answer the prompt in this session — omit out_dir to read the documents into the conversation, or name a folder inside the working directory.
