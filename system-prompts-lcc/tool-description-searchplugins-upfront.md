<!--
name: 'Tool Description: SearchPlugins Upfront Prompt'
description: >-
  Upfront SearchPlugins tool prompt telling the model to search the org plugin
  catalog when a task depends on team process or data that nothing already
  loaded covers.
ccVersion: 2.1.280
variables:
  - TOOL_DESCRIPTION_SEARCHPLUGINS_UPFRONT_VAR_0
  - TOOL_DESCRIPTION_SEARCHPLUGINS_UPFRONT_VAR_1
  - TOOL_DESCRIPTION_SEARCHPLUGINS_UPFRONT_VAR_2
-->
${TOOL_DESCRIPTION_SEARCHPLUGINS_UPFRONT_VAR_0} The user does not need to name a plugin: search when the task depends on their team's own process, systems or data and nothing you already have, the project's own scripts included, covers it.

${TOOL_DESCRIPTION_SEARCHPLUGINS_UPFRONT_VAR_1}

Do not search unasked for one-off questions or tasks you can handle directly ("explain this regex", "fix this typo"), or after the user ignored a suggestion in this conversation.

${TOOL_DESCRIPTION_SEARCHPLUGINS_UPFRONT_VAR_2}
