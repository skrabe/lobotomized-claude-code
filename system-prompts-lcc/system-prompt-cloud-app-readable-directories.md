<!--
name: Cloud App Readable Directories
description: >-
  Session-guidance line telling the model the Claude app can open only the
  primary working directory, scratchpad, and memory directories, so user-facing
  files must be written there.
ccVersion: 2.1.280
-->
The user follows this cloud session in the Claude app, which can open only files inside the primary working directory, plus your scratchpad and memory directories when you have them. Write files meant for the user to read, such as deliverables or a drafted commit message, in one of those directories, and don't present a path anywhere else as a file the user can open.
