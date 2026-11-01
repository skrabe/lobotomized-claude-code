<!--
name: 'Tool result: Bash command text carrier lost'
description: >-
  Bash output replacement when a startup file unset the variable carrying the
  command text, so the command was not run.
ccVersion: 2.1.316
-->
Claude Code did not run this command: something that the shell runs first (a hook's environment file, say) removed the variable that held the command's text. Run it again: commands are now passed on the shell's command line instead.
