<!--
name: Write to git-internal path then run git
description: >-
  Command-safety approval reason surfaced to the model warning a command writes
  git-internal paths that git may execute.
ccVersion: 2.1.206
-->
Command writes to a git-internal path (HEAD, objects/, refs/, hooks/, .git/) and runs git. This could plant a malicious hook that git then executes.
