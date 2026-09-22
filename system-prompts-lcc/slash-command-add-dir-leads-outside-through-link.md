<!--
name: 'Slash Command: /add-dir — path leads outside through a link'
description: >-
  Tells the model the path is a link resolving outside the working directory, so
  nested skills were not loaded, and names the /add-dir target that would grant
  access.
ccVersion: 2.1.257
variables:
  - SLASH_COMMAND_ADD_DIR_LEADS_OUTSIDE_THROUGH_LINK_VAR_0
  - SLASH_COMMAND_ADD_DIR_LEADS_OUTSIDE_THROUGH_LINK_VAR_1
  - SLASH_COMMAND_ADD_DIR_LEADS_OUTSIDE_THROUGH_LINK_VAR_2
-->
${SLASH_COMMAND_ADD_DIR_LEADS_OUTSIDE_THROUGH_LINK_VAR_0} leads outside the working directory through a link (it resolves to ${SLASH_COMMAND_ADD_DIR_LEADS_OUTSIDE_THROUGH_LINK_VAR_1.bold(SLASH_COMMAND_ADD_DIR_LEADS_OUTSIDE_THROUGH_LINK_VAR_2)}), so its skills, commands, and agents weren't loaded. Run /add-dir ${SLASH_COMMAND_ADD_DIR_LEADS_OUTSIDE_THROUGH_LINK_VAR_2} to grant access to it.
