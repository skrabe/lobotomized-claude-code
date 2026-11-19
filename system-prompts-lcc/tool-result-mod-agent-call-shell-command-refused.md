<!--
name: 'Tool Result: Mod agent.call shell command refused'
description: >-
  Deny message when a mod tries to run a shell command with $.agent.call in a
  session whose safety check judges only Claude's own calls
ccVersion: 2.1.328
-->
A mod can't run a shell command with $.agent.call in this session, because this session's safety check judges only the calls that Claude writes.
