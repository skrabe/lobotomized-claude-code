<!--
name: 'Data: allowManagedPermissionRulesOnly setting description'
description: >-
  Description of the `allowManagedPermissionRulesOnly` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.282
-->
When true (and set in managed settings), permission rules from user, project, local, and --settings files and allow rules from --allowedTools are ignored; only managed settings can add allow rules through settings. The allowed-tools frontmatter of skills and custom commands from user, project, and --add-dir sources, and of plugins Claude Code adopts from a .claude-plugin manifest inside those skills directories, is ignored too; other plugins and managed and bundled skills keep theirs. --disallowedTools, skill disallowed-tools, and other deny and ask rules from the command line or the current session still apply.
