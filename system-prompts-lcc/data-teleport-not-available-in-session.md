<!--
name: 'Data: /teleport unavailable in this session'
description: >-
  Explanatory stdout returned for /teleport on a headless/cloud surface; wrapped
  in <local-command-stdout> and pushed into the conversation, so the model reads
  it and relays the instruction.
ccVersion: 2.1.224
variables:
  - DATA_TELEPORT_NOT_AVAILABLE_IN_SESSION_VAR_0
-->
/teleport pulls a cloud session into a terminal on your own machine, so it can't run from inside this session. To continue this session locally, run claude --teleport ${DATA_TELEPORT_NOT_AVAILABLE_IN_SESSION_VAR_0} from a checkout of this repository.
