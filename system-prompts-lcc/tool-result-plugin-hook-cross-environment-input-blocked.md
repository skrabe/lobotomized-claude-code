<!--
name: Cross-environment hook input blocked
description: >-
  Denies a tool call when a hook from another environment tries to change its
  input.
ccVersion: 2.1.295
-->
A plugin hook changed this tool call's input. That is allowed only for calls that run in the same environment as the hook, and this one does not, so the call was not made. Retrying will not help while the hook keeps changing the input. Go on without this call, and tell the user that a hook in one of their plugins changes this tool's input, which is not supported here.
