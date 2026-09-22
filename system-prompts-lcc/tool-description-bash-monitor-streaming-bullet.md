<!--
name: 'Tool Description: Bash Monitor Streaming Bullet'
description: >-
  Bash tool guidance bullet telling the model to use the Monitor tool to stream
  background-process events, vs Bash run_in_background for one-shot waits.
ccVersion: 2.1.178
-->
Use the Monitor tool to stream events from a background process (each stdout line is a notification). For one-shot "wait until done," use Bash with run_in_background instead.
