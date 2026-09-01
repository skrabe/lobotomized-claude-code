<!--
name: 'Data: Agent Import — Project-Scope Config Held Back'
description: >-
  Prompt line explaining that project-level foreign config is neither listed nor
  imported by `--yes`; part of the `/import` query prompt sent to the model.
ccVersion: 2.1.214
variables:
  - DATA_AGENT_IMPORT_PROJECT_SCOPE_HELD_BACK_VAR_0
  - DATA_AGENT_IMPORT_PROJECT_SCOPE_HELD_BACK_VAR_1
-->
Project-level config: ${DATA_AGENT_IMPORT_PROJECT_SCOPE_HELD_BACK_VAR_0} ${DATA_AGENT_IMPORT_PROJECT_SCOPE_HELD_BACK_VAR_1(DATA_AGENT_IMPORT_PROJECT_SCOPE_HELD_BACK_VAR_0,"item")} from this repo's \`.codex/\` or \`.gemini/\` directory. These stay unlisted and \`--yes\` skips them — project config can be authored by anyone with write access to the repo. Tell the user to run \`claude import\` from a terminal to review them individually.
