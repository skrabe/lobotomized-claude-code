<!--
name: 'Tool Description: REPL'
description: >-
  Describes the REPL tool, a JavaScript programming interface for looping,
  branching, and composing Claude Code tool calls as async functions
ccVersion: 2.1.218
variables:
  - SHELL_TOOL_NAME
  - IS_MCP_TOOL_ERROR_THROW_ENABLED
  - IS_BASH_ENV
  - TEMP_FILE_HEREDOC_COMMAND_EXAMPLE
-->
REPL is your programming interface to Claude Code's tools. Use it to loop, branch, and compose tool calls in JavaScript when that's clearer than repeated individual calls. Batch the work into ONE REPL call — write one complete async script, not several separate calls.

Tools are async functions: \`Read\`, \`Write\`, \`Edit\`, \`Glob\`, \`Grep\`, \`${SHELL_TOOL_NAME}\`, etc. MCP tools are callable by full name (e.g. \`await mcp__slack__slack_send_message({...})\`).${IS_MCP_TOOL_ERROR_THROW_ENABLED?" Built-in tools resolve with `{error: string}` on failure; MCP tool calls throw — catch only where the script can proceed without the result.":""}

\`\`\`javascript
const { filenames } = await Glob({ pattern: 'src/**/*.ts' })
for (const f of filenames) {
  const { file } = await Read({ file_path: f })
  if (file.content.includes('oldName')) {
    await Edit({ file_path: f, old_string: 'oldName', new_string: 'newName', replace_all: true })
  }
}
const { stdout } = await ${SHELL_TOOL_NAME}({ command: 'git status' })
\`\`\`

Tips:
- \`import\`/\`require\` don't work — the vm context is sealed. Use \`Read\`/\`Write\`/\`Glob\` for the filesystem and \`${SHELL_TOOL_NAME}\` for shell.
- Use \`Promise.all()\` for parallel operations
- Variables persist across REPL calls; the last expression is the result
- \`haiku(prompt, schema?)\` — one-turn model sampling. No schema returns text; a JSON schema returns the parsed object.
- \`registerTool(name, desc, schema, handler)\` defines a tool; \`unregisterTool(name)\`, \`listTools()\`, \`getTool(name)\` manage them
- ${IS_BASH_ENV?`\`shQuote(s)\` quotes a string for Bash — use this instead of \`JSON.stringify\` (double quotes don't protect backticks or \`$\`)
- Don't write a temp file just to feed a shell command — pipe via heredoc: \`await ${SHELL_TOOL_NAME}({command: "${TEMP_FILE_HEREDOC_COMMAND_EXAMPLE}"})\`. Generic temp paths get clobbered by parallel agents.`:"`shQuote(s)` is POSIX-only — for PowerShell, double the single quotes: `\"'\"+s.replaceAll(\"'\", \"''\")+\"'\"`. For multi-line input use a here-string `@'\\n...\\n'@` (closing `'@` at column 0)."}
