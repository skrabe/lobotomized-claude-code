<!--
name: 'Tool Result: Artifact db write denied in plan mode'
description: >-
  Permission denial returned to the model when an artifact database write is
  attempted in plan mode with no interactive consent surface available.
ccVersion: 2.1.224
-->
Database writes from plan mode need a consent surface, and no one can answer the prompt in this session. Keep planning in the plan file and raise the write with the user in chat; do not retry this write in this session.
