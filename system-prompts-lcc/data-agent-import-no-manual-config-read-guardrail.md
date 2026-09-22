<!--
name: 'Data: Agent Import — Do Not Read Foreign Config Guardrail'
description: >-
  Guardrail sentence (xdd) appended to the `/import` query prompt and
  interpolated into the /init CLAUDE.md generation prompt, telling the model not
  to read foreign-agent config itself.
ccVersion: 2.1.214
-->
Do NOT read the foreign-agent config files or write Claude Code config yourself — the deterministic import (triggered by `--yes`) applies the same safe-name and path-traversal guards as the terminal picker.
