<!--
name: 'Data: footerLinksRegexes setting description'
description: >-
  Description of the `footerLinksRegexes` setting in Claude Code's settings JSON
  schema. The model reads it through /update-config and settings validation
  errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
Extra clickable footer badges that appear when a regex matches turn output (tool results and assistant responses). Read from user, flag, and managed settings only; ignored in project .claude/settings.json and local .claude/settings.local.json. At most 5 badges render; the oldest is displaced by newer matches and /clear removes them. Use to surface IDs printed by project CLIs as session links.
