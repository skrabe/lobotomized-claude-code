<!--
name: 'System Reminder: Parallel Write Agent Same Checkout'
description: >-
  Agent-prompt note injected when another write-capable agent is already running
  in this checkout, telling this agent not to clobber its edits.
ccVersion: 2.1.280
-->
Note: another write-capable agent is already running in this same working directory, and parallel agents sharing a checkout can overwrite each other's work. Edit only the files your task requires, re-read a file right before changing it, and do not revert or overwrite changes you did not make.
