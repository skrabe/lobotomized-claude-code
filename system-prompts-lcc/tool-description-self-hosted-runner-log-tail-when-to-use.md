<!--
name: 'Tool Description: self-hosted runner log tail when to use'
description: >-
  whenToUse for the tool that tails a self-hosted runner log with secret
  redaction
ccVersion: 2.1.325
-->
When you are about to read the recent lines of a self-hosted runner's log file, use it and not a plain read or tail of the file, because it strips secrets from the text before you see it.
