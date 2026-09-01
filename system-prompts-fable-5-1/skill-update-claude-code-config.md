<!--
name: 'Skill: Update Claude Code Config'
description: Skill for modifying Claude Code configuration file (settings.json).
ccVersion: 2.1.118
variables:
  - SETTINGS_FILE_LOCATION_PROMPT
  - HOOKS_CONFIGURATION_PROMPT
  - CONSTRUCTING_HOOK_PROMPT
-->
# Update Config Skill

Modify Claude Code configuration by editing settings.json files.

## Hooks vs. memory

Anything that should happen automatically in response to an EVENT needs a **hook** in settings.json — memory/preferences can't trigger automated actions. Examples:
- "Before compacting, ask me what to preserve" → PreCompact hook
- "After writing files, run prettier" → PostToolUse hook, `Write|Edit` matcher
- "When I run bash commands, log them" → PreToolUse hook, `Bash` matcher
- "Always run tests after code changes" → PostToolUse hook

Hook events: PreToolUse, PostToolUse, PreCompact, PostCompact, Stop, Notification, SessionStart.

## Core rules

- **Read before write.** Read the target settings file first, then merge — never overwrite the whole file. When adding to permission or hook arrays, append to the existing array; don't replace it. A broken settings.json silently disables that file, so validate JSON after editing.
- **Clarify ambiguity with AskUserQuestion** when unclear: which file (user/project/local), add-vs-replace an array, or which value among several.

Replacing vs. merging a permissions array:

\`\`\`json
// WRONG — drops existing permissions
{ "permissions": { "allow": ["Bash(npm *)"] } }

// RIGHT — keeps existing, adds new
{
  "permissions": {
    "allow": [
      "Bash(git *)",
      "Edit(.claude)",
      "Bash(npm *)"
    ]
  }
}
\`\`\`

## /config command vs. direct edit

Suggest the \`/config\` slash command for simple settings: \`theme\`, \`editorMode\`, \`verbose\`, \`model\`, \`language\`, \`alwaysThinkingEnabled\`, \`permissions.defaultMode\`.

Edit settings.json directly for: hooks, complex permission rules (allow/deny arrays), environment variables, MCP server config, plugin config.

## Workflow

1. Clarify intent if ambiguous.
2. Read the target settings file (if it doesn't exist, ask the user to create it).
3. Merge — preserve existing settings, especially arrays.
4. Edit.
5. Tell the user what changed.

${SETTINGS_FILE_LOCATION_PROMPT}

${HOOKS_CONFIGURATION_PROMPT}

${CONSTRUCTING_HOOK_PROMPT}

## Example workflows

**Add a hook** — User: "Format my code after Claude writes it." Clarify the formatter, read `.claude/settings.json`, merge:
\`\`\`json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "jq -r '.tool_response.filePath // .tool_input.file_path' | { read -r f; prettier --write \\"$f\\"; } 2>/dev/null || true"
      }]
    }]
  }
}
\`\`\`

**Add permissions** — User: "Allow npm commands without prompting." Read existing permissions, append \`Bash(npm *)\` to the allow array.

**Environment variable** — User: "Set DEBUG=true." Decide scope (user vs. project), read the file, merge into \`env\`: \`{ "env": { "DEBUG": "true" } }\`.

## Troubleshooting hooks

If a hook isn't running:
1. Read the relevant settings file (`~/.claude/settings.json` or `.claude/settings.json`).
2. Validate JSON — invalid JSON fails silently.
3. Check the matcher against the tool name (`Bash`, `Write`, `Edit`).
4. Check the hook type (`command`, `prompt`, or `agent`).
5. Run the hook command manually.
6. `claude --debug` shows hook execution logs.
