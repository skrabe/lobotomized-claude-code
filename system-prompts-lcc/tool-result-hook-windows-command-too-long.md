<!--
name: 'Hook: command too long on Windows'
description: >-
  Hook command not run because it is too long to pass on Windows; tells Claude
  not to change the hook.
ccVersion: 2.1.332
-->
Claude Code did not run this command: it, or one of its arguments, is too long to pass on Windows, which may cut it so that only its start runs. Move it into a script file and run that, or, if a plugin supplies it, ask the plugin's author to. The user needs to do this; Claude should not change the hook.
