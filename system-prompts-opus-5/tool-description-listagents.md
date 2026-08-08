<!--
name: 'Tool Description: ListAgents'
description: >-
  Model-facing description of the ListAgents tool listing addressable
  subagents/local/remote sessions and how to send messages to them.
ccVersion: 2.1.224
variables:
  - SEND_MESSAGE_TOOL_NAME
  - REMOTE_BRIDGE_REPLY_ONLY_CONSTRAINT
-->
Lists agents you can ${SEND_MESSAGE_TOOL_NAME} to — in-process subagents you spawned, other local Claude sessions on this machine, your Claude sessions running in the cloud (when this session has cloud access), and (when Remote Control is connected) remote bridge sessions, which are reply-only — you can message one ${REMOTE_BRIDGE_REPLY_ONLY_CONSTRAINT}, and no connector reaches it by name either. Names are the address: send with \`${SEND_MESSAGE_TOOL_NAME}({to: "<name>", message: "..."})\`, copying the name exactly as a row prints it. Append a row's \` [ref]\` only when the bare name is not enough — two rows share it, or an error asks you to disambiguate.
