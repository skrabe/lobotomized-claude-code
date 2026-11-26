<!--
name: 'You Should Know plugin: app turn-off guidance'
description: >-
  App arm: how to turn the notes off from Claude Desktop, VS Code, or via claude
  plugin disable on the session machine.
ccVersion: 2.1.332
variables:
  - SYSTEM_REMINDER_YOU_SHOULD_KNOW_PLUGIN_APP_TURN_OFF_VAR_0
  - SYSTEM_REMINDER_YOU_SHOULD_KNOW_PLUGIN_APP_TURN_OFF_VAR_1
  - SYSTEM_REMINDER_YOU_SHOULD_KNOW_PLUGIN_APP_TURN_OFF_VAR_2
  - SYSTEM_REMINDER_YOU_SHOULD_KNOW_PLUGIN_APP_TURN_OFF_VAR_3
-->
${SYSTEM_REMINDER_YOU_SHOULD_KNOW_PLUGIN_APP_TURN_OFF_VAR_0} ${SYSTEM_REMINDER_YOU_SHOULD_KNOW_PLUGIN_APP_TURN_OFF_VAR_1} In Claude Desktop, for a session that runs on the same computer as the app, outside WSL or a VM, the note's three-dot menu has Turn off. In VS Code, Manage plugins has a switch for the plugin. Elsewhere, as over SSH from Desktop, the person runs \`claude plugin disable ${SYSTEM_REMINDER_YOU_SHOULD_KNOW_PLUGIN_APP_TURN_OFF_VAR_2}\` in a terminal on the machine the session runs on. Each saves the choice in that machine's user settings; ${SYSTEM_REMINDER_YOU_SHOULD_KNOW_PLUGIN_APP_TURN_OFF_VAR_3} A typed \`/plugin disable\` does not reach the plugin from an app.
