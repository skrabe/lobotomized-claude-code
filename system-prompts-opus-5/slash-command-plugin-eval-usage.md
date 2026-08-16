<!--
name: 'Slash Command: /plugin eval — usage'
description: >-
  Teaches the model how /plugin eval is invoked and that each evals/*.md file
  needs `query` and `should_trigger` frontmatter with at least five recommended,
  which is what it needs to author or fix eval files.
ccVersion: 2.1.233
-->
Usage: /plugin eval [path]

Run trigger evaluations for a skill against the queries in its evals/ folder.

Examples:
  /plugin eval ./my-skill
  /plugin eval ~/.claude/skills/pdf-tools

Each evals/*.md file needs frontmatter with \`query\` (string)
and \`should_trigger\` (boolean). The spec recommends at least five.

Or from the command line:
  claude plugin eval [path]
