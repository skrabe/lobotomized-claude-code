<!--
name: 'Skill: update-config description'
description: 'Update-config skill description (settings.json hooks, perms, env)'
ccVersion: 2.1.141
-->
Use this skill to configure the Claude Code harness via settings.json. Automated behaviors ("from now on when X", "each time X", "whenever X", "before/after X") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions ("allow X", "add permission", "move permission to"), env vars ("set X=Y"), hook troubleshooting, or any changes to settings.json/settings.local.json files. For simple settings like theme/model, suggest the /config command.
