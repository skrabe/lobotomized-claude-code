<!--
name: 'Tool Result: Steward own-branch merge unchecked file'
description: >-
  Refuses a non-base merge that brings a file gh, git or Claude Code may run
  unchecked
ccVersion: 2.1.330
-->
the merge would bring or change a file or link that gh, git, Claude Code or a Claude Code hook may run or read, and nothing would check it first. If somebody has merged the base into the branch on GitHub, such a file may come from there: fetch and merge the base first, as listed, then run this merge once more. If it is refused again, leave it to the user for the rest of this run: tell them that the branch needs it, and why you did not make it
