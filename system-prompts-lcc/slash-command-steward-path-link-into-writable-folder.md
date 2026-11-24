<!--
name: 'Slash Command: Steward PATH link into writable folder'
description: >-
  Steward refusal template when a program on PATH is a link leading into a
  writable folder
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_STEWARD_PATH_LINK_INTO_WRITABLE_FOLDER_VAR_0
  - SLASH_COMMAND_STEWARD_PATH_LINK_INTO_WRITABLE_FOLDER_VAR_1
-->
in a folder of your PATH, gh, git, or a program that they call is a link that leads into ${SLASH_COMMAND_STEWARD_PATH_LINK_INTO_WRITABLE_FOLDER_VAR_0}, where this session can write, so it isn't clear which gh and git an unattended watch would run. Point that link at a file outside ${SLASH_COMMAND_STEWARD_PATH_LINK_INTO_WRITABLE_FOLDER_VAR_1}
