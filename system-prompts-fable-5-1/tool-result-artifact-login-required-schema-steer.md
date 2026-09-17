<!--
name: 'Tool Result: Artifact Login Required Schema Steer'
description: >-
  Artifact schema-steer note: every Artifact call is refused until a claude.ai
  login exists, so the schema error only matters after login.
ccVersion: 2.1.274
-->
Changing the input will not help: every Artifact call is refused like this until a claude.ai login is available, so do not retry; tell the user what is needed. The input was also invalid, but the schema error below matters only once that login is available.
