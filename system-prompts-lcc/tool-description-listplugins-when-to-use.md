<!--
name: 'Tool Description: ListPlugins when to use'
description: When-to-use line for listing the user's claude.ai plugins.
ccVersion: 2.1.325
variables:
  - TOOL_DESCRIPTION_LISTPLUGINS_WHEN_TO_USE_VAR_0
  - TOOL_DESCRIPTION_LISTPLUGINS_WHEN_TO_USE_VAR_1
-->
When the user asks which plugins they have on claude.ai, or you are about to say what was installed after a ${TOOL_DESCRIPTION_LISTPLUGINS_WHEN_TO_USE_VAR_0} card, use it; it omits plugins installed locally with /plugin; for plugins they lack, use ${TOOL_DESCRIPTION_LISTPLUGINS_WHEN_TO_USE_VAR_1}.
