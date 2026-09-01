<!--
name: 'Tool Result: set_cwd busy (turn in progress)'
description: >-
  Message value in the set_cwd tool's busy rejection returned to the model when
  a turn is in progress, telling it to wait or interrupt then retry;
  model-facing.
ccVersion: 2.1.201
-->
A turn is in progress — the working directory can only change while the session is idle. Wait for the turn to finish (or interrupt it), then retry.
