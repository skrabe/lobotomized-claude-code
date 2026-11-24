<!--
name: 'Steward stop: nothing to stop'
description: >-
  Reply to /steward stop when this session isn't watching, with how to stop a
  watch started in another conversation.
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_STEWARD_STOP_NOTHING_TO_WATCH_VAR_0
  - SLASH_COMMAND_STEWARD_STOP_NOTHING_TO_WATCH_VAR_1
-->
Nothing to stop. This session isn't watching a pull request.${SLASH_COMMAND_STEWARD_STOP_NOTHING_TO_WATCH_VAR_0()?` If you started a watch in another conversation, it may still be on: open that conversation from the history of the tab or side bar where you started it, then type ${SLASH_COMMAND_STEWARD_STOP_NOTHING_TO_WATCH_VAR_1} there. Or reload the window.`:""}
