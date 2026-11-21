<!--
name: 'Tool Result: Mod agent.call refused'
description: >-
  Deny message when a mod makes a call with $.agent.call in a session whose
  safety check judges only Claude's own calls.
ccVersion: 2.1.330
-->
A mod can't make this call with $.agent.call in this session, because this session's safety check judges only the calls that Claude writes.
