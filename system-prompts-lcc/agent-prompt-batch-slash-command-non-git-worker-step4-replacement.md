<!--
name: 'Agent Prompt: /batch non-git worker step 4 replacement'
description: >-
  Instruction spliced into the /batch non-git version control section: tell
  every worker the directory is not git and replace step 4 with publishing
  through the project's own VCS, ending with `PR: none — <what was published
  instead>`.
ccVersion: 2.1.330
-->
Say so in every worker prompt, and when you copy the worker instructions, replace step 4 with: commit and publish the change with this project's own version-control commands, and end with `PR: none — <what was published instead>` when no pull request can be opened.
