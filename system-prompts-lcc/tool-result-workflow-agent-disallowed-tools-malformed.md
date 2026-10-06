<!--
name: 'Tool Result: workflow agent() disallowedTools malformed'
description: >-
  Error thrown into a workflow script when agent() opts.disallowedTools is not
  an array of non-empty tool-name strings; the spawn is refused.
ccVersion: 2.1.291
-->
agent() opts.disallowedTools must be an array of non-empty tool-name strings (e.g. ['Bash', 'Write']); got 
