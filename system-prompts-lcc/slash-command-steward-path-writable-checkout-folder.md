<!--
name: 'Slash Command: Steward - PATH holds writable checkout folder'
description: >-
  /steward reason that PATH holds a writable folder of this checkout, with
  advice to start claude without it.
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_STEWARD_PATH_WRITABLE_CHECKOUT_FOLDER_VAR_0
  - SLASH_COMMAND_STEWARD_PATH_WRITABLE_CHECKOUT_FOLDER_VAR_1
-->
your PATH includes ${SLASH_COMMAND_STEWARD_PATH_WRITABLE_CHECKOUT_FOLDER_VAR_0===void 0?"":`${SLASH_COMMAND_STEWARD_PATH_WRITABLE_CHECKOUT_FOLDER_VAR_0}, `}a folder in this checkout that this session can write to, ${SLASH_COMMAND_STEWARD_PATH_WRITABLE_CHECKOUT_FOLDER_VAR_1===void 0?"so it isn't clear which gh and git an unattended watch would run":"and gh, git, or a program that they or Claude Code calls is in it, so it isn't clear which gh and git would run"}. Start claude from a shell without that folder${SLASH_COMMAND_STEWARD_PATH_WRITABLE_CHECKOUT_FOLDER_VAR_0===void 0?", which echo $PATH shows":""} (for a Python venv, run deactivate first, and don't start claude through npx or a package script)
