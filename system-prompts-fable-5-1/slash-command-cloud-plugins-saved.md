<!--
name: 'Slash Command: /cloud-plugins Saved'
description: >-
  Confirmation the /cloud-plugins local-jsx command returns via onDone after
  persisting whether this machine's plugins are used in cloud sessions.
ccVersion: 2.1.247
variables:
  - SLASH_COMMAND_CLOUD_PLUGINS_SAVED_VAR_0
  - SLASH_COMMAND_CLOUD_PLUGINS_SAVED_VAR_1
-->
Saved: ${SLASH_COMMAND_CLOUD_PLUGINS_SAVED_VAR_0==="accepted"?"cloud sessions from this machine use your enabled plugins — the ones attached from this terminal now, new ones from the start":SLASH_COMMAND_CLOUD_PLUGINS_SAVED_VAR_1==="accepted"?"your plugins stay on this machine from now on — nothing more is sent from this terminal, and a session already using them keeps them only until it restarts":"your plugins stay on this machine; cloud sessions load only the repository’s and your organization’s plugins"}. Run /cloud-plugins again to change it.
