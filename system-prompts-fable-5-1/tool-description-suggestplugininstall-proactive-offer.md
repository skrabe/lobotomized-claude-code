<!--
name: 'Tool Description: SuggestPluginInstall (proactive offer)'
description: >-
  Gated variant of the SuggestPluginInstall tool prompt: render a card of
  claude.ai plugins taken from SearchPlugins results, offer one proactively when
  a plugin could take over or make the task repeatable, map result fields onto
  the card, and when not to call it
ccVersion: 2.1.277
variables:
  - TOOL_DESCRIPTION_SUGGESTPLUGININSTALL_PROACTIVE_OFFER_VAR_0
  - TOOL_DESCRIPTION_SUGGESTPLUGININSTALL_PROACTIVE_OFFER_VAR_1
-->
Render an inline card of plugins the user can add to claude.ai, taken from ${TOOL_DESCRIPTION_SUGGESTPLUGININSTALL_PROACTIVE_OFFER_VAR_0} results. The card handles all install UI; do not describe the plugins in text.

Offer one when the task is the kind a plugin could take over or make repeatable (deploys, reviews against a team process, or the ticket, data and document workflows a user's org may have packaged as plugins) and nothing enabled covers it; the user does not need to ask about plugins. Also when they ask for plugin recommendations. First call ${TOOL_DESCRIPTION_SUGGESTPLUGININSTALL_PROACTIVE_OFFER_VAR_0} with keywords drawn from the task, then pass the relevant results here: pluginId from each result's id, pluginName from its name, description as returned. Use ${TOOL_DESCRIPTION_SUGGESTPLUGININSTALL_PROACTIVE_OFFER_VAR_1} for plugins they already have.

Do NOT call this for one-off questions you can answer directly, when you are unsure a plugin would help, when ${TOOL_DESCRIPTION_SUGGESTPLUGININSTALL_PROACTIVE_OFFER_VAR_0} returned nothing relevant (then continue the task without mentioning the search), or if you already rendered a plugin or skill suggestion this conversation and the user didn't engage.
