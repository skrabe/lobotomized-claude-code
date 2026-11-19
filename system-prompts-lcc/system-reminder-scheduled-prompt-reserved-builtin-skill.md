<!--
name: 'System Reminder: Scheduled prompt reserved for built-in skill'
description: >-
  Tells Claude a scheduled prompt ran nothing because its line names a built-in
  skill, and how to tell the user
ccVersion: 2.1.328
-->
This scheduled prompt ran nothing: this line is reserved for a skill built into Claude Code, which did not run here, and a timer runs no other command in its place. Do not do the work another way, and do not schedule this prompt again. Tell the user in one line that it was skipped and why, and that they can cancel the timer if it repeats. If it is a command of their own, say that it needs another name to run on a timer.
