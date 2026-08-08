<!--
name: 'Tool Result: Artifact database read blocked in plan mode'
description: >-
  Permission denial returned to the model when the Artifact tool tries to read
  another person's artifact database in plan mode with no live consent surface.
ccVersion: 2.1.224
-->
Reads from another person's artifact database in plan mode need a consent surface, and no one can answer the prompt in this session. Keep planning in the plan file and raise the read with the user in chat; do not retry this read in this session.
