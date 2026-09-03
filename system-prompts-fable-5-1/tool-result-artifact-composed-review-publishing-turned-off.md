<!--
name: Composed Review Publishing Turned Off
description: >-
  Artifact tool error returned to the model when composed pr_review publishing
  was disabled by an operator mid-session, telling it to retry later rather than
  loop.
ccVersion: 2.1.219
-->
composed review publishing was turned off by an operator during this session — this gate re-checks the live switch, so retry after a few minutes, or start a new session once it is restored. Do not retry in a tight loop.
