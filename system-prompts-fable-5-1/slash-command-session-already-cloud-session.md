<!--
name: 'Slash Command: Session Already Cloud Session'
description: >-
  local-command-stdout returned for /session when this session is already a
  cloud session, telling the model to continue locally with claude --teleport.
ccVersion: 2.1.274
variables:
  - SLASH_COMMAND_SESSION_ALREADY_CLOUD_SESSION_VAR_0
  - SLASH_COMMAND_SESSION_ALREADY_CLOUD_SESSION_VAR_1
-->
This session is already running as a cloud session: ${SLASH_COMMAND_SESSION_ALREADY_CLOUD_SESSION_VAR_0(SLASH_COMMAND_SESSION_ALREADY_CLOUD_SESSION_VAR_1)}. To continue it in your terminal, run claude --teleport ${SLASH_COMMAND_SESSION_ALREADY_CLOUD_SESSION_VAR_1} from a checkout of this repository.
