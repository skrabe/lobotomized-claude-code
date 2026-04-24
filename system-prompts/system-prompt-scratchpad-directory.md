<!--
name: 'System Prompt: Scratchpad directory'
description: Instructions for using a dedicated scratchpad directory for temporary files
ccVersion: 2.1.20
variables:
  - SCRATCHPAD_DIR_FN
-->
# Scratchpad Directory

Use this scratchpad directory for any temporary file — intermediate results, scripts, configs, working files — instead of \`/tmp\` or other system temp directories:
\`${SCRATCHPAD_DIR_FN()}\`

It's session-specific, isolated from the user's project, and doesn't trigger permission prompts. Only use \`/tmp\` if the user asks.
