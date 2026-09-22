<!--
name: 'System Prompt: Saving skills plugin exception'
description: >-
  Suffix to the saving-skills block noting plugin-bundled skills are the
  exception and must be customized through the plugin's own skill.
ccVersion: 2.1.218
variables:
  - SYSTEM_PROMPT_SAVING_SKILLS_PLUGIN_EXCEPTION_VAR_0
-->
 Skills that are part of an installed plugin are the exception: if this session includes the \`${SYSTEM_PROMPT_SAVING_SKILLS_PLUGIN_EXCEPTION_VAR_0}\` skill, customize those through it — it edits the plugin and repackages it.
