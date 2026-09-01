<!--
name: 'Data: Import Unmappable — Project-Level Items Withheld'
description: >-
  Section emitted by yA_() into the generated import-to-claude-code SKILL.md
  explaining that project-scope unmapped items are deliberately not listed.
ccVersion: 2.1.214
variables:
  - DATA_IMPORT_UNMAPPABLE_PROJECT_SCOPE_ITEMS_NOT_LISTED_VAR_0
  - DATA_IMPORT_UNMAPPABLE_PROJECT_SCOPE_ITEMS_NOT_LISTED_VAR_1
  - DATA_IMPORT_UNMAPPABLE_PROJECT_SCOPE_ITEMS_NOT_LISTED_VAR_2
-->
There ${DATA_IMPORT_UNMAPPABLE_PROJECT_SCOPE_ITEMS_NOT_LISTED_VAR_0.length===1?"is":"are"} also ${DATA_IMPORT_UNMAPPABLE_PROJECT_SCOPE_ITEMS_NOT_LISTED_VAR_0.length} unmapped ${DATA_IMPORT_UNMAPPABLE_PROJECT_SCOPE_ITEMS_NOT_LISTED_VAR_1(DATA_IMPORT_UNMAPPABLE_PROJECT_SCOPE_ITEMS_NOT_LISTED_VAR_0.length,"item")} from the project-level ${DATA_IMPORT_UNMAPPABLE_PROJECT_SCOPE_ITEMS_NOT_LISTED_VAR_2.displayName} config in the repo where the import ran. Those are not listed here (project config can be authored by anyone with write access to that repo). If you still need them, re-open that project and review its \`.codex/\` or \`.gemini/\` directory directly.
