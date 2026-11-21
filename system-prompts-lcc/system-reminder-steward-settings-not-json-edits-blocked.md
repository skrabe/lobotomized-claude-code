<!--
name: 'System Reminder: Steward settings not JSON edits blocked'
description: Blocks edits while a checkout settings or .mcp.json file isn't valid JSON
ccVersion: 2.1.330
-->
one of this checkout's .claude/settings.json, .claude/settings.local.json and .mcp.json files isn't JSON now, as with a merge's conflict marks in it, so Claude Code can't tell which files it would run. No file is edited until it is JSON again. Tell the user
