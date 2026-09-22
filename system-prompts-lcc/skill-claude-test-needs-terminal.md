<!--
name: Skill Claude Test Needs Terminal
description: >-
  Claude Test skill.prompt/command.run failure telling the model to relay that
  the browser helper only starts from an interactive terminal session.
ccVersion: 2.1.274
-->
Claude Test needs an interactive Claude Code session in a terminal. It starts its browser helper by reloading plugins, and only a terminal session starts a plugin helper on a reload. Run claude in the project folder and type /claude-test there.
