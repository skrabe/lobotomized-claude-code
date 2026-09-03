<!--
name: Artifact Comments Thread ID and Cursor Conflict
description: >-
  Tool validation result telling the model that reading one thread and
  continuing a paginated thread list cannot be requested together.
ccVersion: 2.1.226
-->
`thread_id` (read one thread) and `cursor` (continue the list) cannot be combined — pass one.
