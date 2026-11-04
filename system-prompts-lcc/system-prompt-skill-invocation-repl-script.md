<!--
name: 'System Prompt: Skill invocation via REPL script'
description: >-
  REPL-mode arm of the skill-invocation guidance: invoke /<skill-name> with
  tools.Skill from a script, only listed skills.
ccVersion: 2.1.318
-->
When the user types `/<skill-name>`, invoke it with `tools.Skill` from a script. Only use skills listed in the user-invocable skills section — don't guess.
