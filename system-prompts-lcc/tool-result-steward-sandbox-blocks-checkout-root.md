<!--
name: 'Tool Result: Steward sandbox blocks checkout root'
description: >-
  Leaves the merge to the user when the sandbox cannot write the checkout's top
  folder
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_STEWARD_SANDBOX_BLOCKS_CHECKOUT_ROOT_VAR_0
-->
Claude Code's sandbox doesn't let this checkout's top folder be written in this session, which may have started in a lower folder. git runs inside the sandbox, so every merge is the user's. Tell them once that they can merge ${TOOL_RESULT_STEWARD_SANDBOX_BLOCKS_CHECKOUT_ROOT_VAR_0} in this checkout, in a terminal of their own, and push it themselves, and that if their merge ends this watch, they run /steward again. Or they can run /steward stop here, start Claude Code in the top folder and run /steward there. Don't try a merge again in this watch
