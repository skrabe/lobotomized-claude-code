<!--
name: 'Plugin validate: engine.create hook outside form'
description: >-
  Plugin validate message that an engine.create hook is outside its supported
  form, with the form to use.
ccVersion: 2.1.325
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_ENGINE_CREATE_HOOK_OUTSIDE_FORM_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_ENGINE_CREATE_HOOK_OUTSIDE_FORM_VAR_1
  - SLASH_COMMAND_PLUGIN_VALIDATE_ENGINE_CREATE_HOOK_OUTSIDE_FORM_VAR_2
  - SLASH_COMMAND_PLUGIN_VALIDATE_ENGINE_CREATE_HOOK_OUTSIDE_FORM_VAR_3
-->
${SLASH_COMMAND_PLUGIN_VALIDATE_ENGINE_CREATE_HOOK_OUTSIDE_FORM_VAR_0}${SLASH_COMMAND_PLUGIN_VALIDATE_ENGINE_CREATE_HOOK_OUTSIDE_FORM_VAR_1}: this engine.create hook is outside its form: ${SLASH_COMMAND_PLUGIN_VALIDATE_ENGINE_CREATE_HOOK_OUTSIDE_FORM_VAR_2(SLASH_COMMAND_PLUGIN_VALIDATE_ENGINE_CREATE_HOOK_OUTSIDE_FORM_VAR_3,300)}. Spell it one way: on('engine.create', async ($, e, next) => { const { fs, process, ...beneath } = await next(e); /* any statements that don't return */ return { ...beneath, voice: voiceOf() } }). Validate lists what a hook in this form does if it registers and doesn't throw. It can't say what this module adds to or withholds from $.
