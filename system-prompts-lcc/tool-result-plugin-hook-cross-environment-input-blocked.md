<!--
name: Cross-environment hook input blocked
description: >-
  Denies a tool call when a hook from another environment tries to change its
  input.
ccVersion: 2.1.294
-->
A plugin hook tried to change this tool call's input. It may do that only for tools that run in the same environment as the hook, and this tool does not, so the call was not made. Retrying will not help while the hook keeps changing the input: go on without this call, and tell the user that a plugin hook blocked it.
