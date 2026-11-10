<!--
name: 'Tool Result: Connector upload malformed request state'
description: >-
  Reason in the connector-upload error when requestState is missing, empty, not
  text or over 65,536 characters
ccVersion: 2.1.322
-->
its requestState is missing, not text, empty, or longer than 65,536 characters; the files extension has the server bind the call to a requestState, which Claude Code sends back unchanged when it calls again
