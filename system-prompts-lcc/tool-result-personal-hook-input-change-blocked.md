<!--
name: 'Tool Result: Personal Hook Input Change Blocked'
description: >-
  Reports a restricted personal hook input change and instructs the model to
  continue without the call.
ccVersion: 2.1.295
-->
A hook from the user's own Claude Code files tried to change this tool call's input. In this session such hooks may block or ask about a call but not change it, so the call was not made. Retrying will not help while the hook keeps changing the input: go on without this call, and tell the user their hook's change to it was refused.
