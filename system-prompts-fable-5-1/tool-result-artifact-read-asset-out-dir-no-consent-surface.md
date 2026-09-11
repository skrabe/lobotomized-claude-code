<!--
name: Artifact Read Asset Out Dir No Consent Surface
description: >-
  checkPermissions deny for read_asset out_dir outside working folders when no
  one can answer the prompt.
ccVersion: 2.1.268
-->
read_asset saves outside this session’s working folders only with the user’s approval, and no one can answer the prompt in this session — omit out_dir so the asset lands in the working directory, or raise it with the user in chat.
