<!--
name: 'Slash Command: Steward - PATH holds writable checkout folder'
description: >-
  /steward reason that PATH holds a writable folder of this checkout, with
  advice to start claude without it.
ccVersion: 2.1.330
variables:
  - SLASH_COMMAND_STEWARD_PATH_WRITABLE_CHECKOUT_FOLDER_VAR_0
  - SLASH_COMMAND_STEWARD_PATH_WRITABLE_CHECKOUT_FOLDER_VAR_1
-->
your PATH holds ${SLASH_COMMAND_STEWARD_PATH_WRITABLE_CHECKOUT_FOLDER_VAR_0===void 0?"":`${SLASH_COMMAND_STEWARD_PATH_WRITABLE_CHECKOUT_FOLDER_VAR_0}, `}a folder of this checkout that I could write to, ${SLASH_COMMAND_STEWARD_PATH_WRITABLE_CHECKOUT_FOLDER_VAR_1===void 0?"so with nobody looking I couldn't tell which gh and git would run":"and gh, git, or a program that they call lies in it, so I can't tell which gh and git would run"}. Start claude from a shell without that folder${SLASH_COMMAND_STEWARD_PATH_WRITABLE_CHECKOUT_FOLDER_VAR_0===void 0?", which echo $PATH shows":""} (for a Python venv, run deactivate first, and don't start it through npx or a package script)
