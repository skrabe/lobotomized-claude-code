<!--
name: 'Tool Result: Projects OAuth Lock Contended'
description: >-
  Precondition failure text returned by the Projects tool's auth-reason switch
  ($Jg) when another Claude Code process holds the OAuth refresh lock; thrown as
  ProjectsPreconditionError from the tool's call and delivered to the model
  inside a <tool_use_error> tool_result.
ccVersion: 2.1.211
-->
Another Claude Code process is refreshing the OAuth token. Retry in a moment.
