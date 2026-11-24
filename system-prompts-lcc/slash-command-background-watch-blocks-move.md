<!--
name: 'Slash command: background blocked by watch'
description: >-
  /background refusal when a watch or its limits are active, telling the action
  needed before moving the session to the background.
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_BACKGROUND_WATCH_BLOCKS_MOVE_VAR_0
  - SLASH_COMMAND_BACKGROUND_WATCH_BLOCKS_MOVE_VAR_1
  - SLASH_COMMAND_BACKGROUND_WATCH_BLOCKS_MOVE_VAR_2
-->
${SLASH_COMMAND_BACKGROUND_WATCH_BLOCKS_MOVE_VAR_0.ended||SLASH_COMMAND_BACKGROUND_WATCH_BLOCKS_MOVE_VAR_1?"The watch's limits still hold":"A watch is on"}. ${SLASH_COMMAND_BACKGROUND_WATCH_BLOCKS_MOVE_VAR_2} before moving this session to the background.
