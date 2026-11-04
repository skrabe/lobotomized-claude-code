<!--
name: 'Skill: plugin-authoring'
description: >-
  Bundled plugin-authoring skill — Make a mod: a change to Claude's own
  interface or behaviour, such as a live pane or panel, a band above the prompt,
  a status line, a toast, a slash command, or a hook on tool calls or prompts.
  Use to make, change or debug a mod or its hooks module.
ccVersion: 2.1.318
-->
---
name: plugin-authoring
description: "Make a mod: a change to Claude's own interface or behaviour, such as a panel or pane that stays beside the chat and updates, a band, status line, toast, slash command, or hook on tool calls. Use to make, change or debug a mod or its hooks module."
---

WHERE TO WRITE IT. Write each mod in its own child folder, \`\${CLAUDE_DEV_MODS_DIR}/<mod-name>/\`, three files written directly:

- \`.claude-plugin/plugin.json\`: \`{ "name": "<mod-name>", "version": "0.1.0", "description": "<one line>" }\`
- \`hooks/hooks.json\`: \`{ "modules": ["./register.tsx"] }\`, one path, relative to that file
- \`hooks/register.tsx\` (or \`.ts\`): the hooks module, \`export const register: Register = (on, options) => { ... }\`, the type imported from \`'claude-code'\`

A mod that keeps values in \`$.state\` has a fourth file, \`types/index.d.ts\`: its type contract, declaring each value in \`interface PluginState\` under the mod's name, named in \`plugin.json\` as \`"types": "./types/index.d.ts"\`. The module imports its value types from \`'../types'\`, and \`claude plugin validate\` holds every \`$.state\` key the module names to that contract.

WHERE THE TYPES ARE. The engine writes them; there is no command to run. Before the mod has loaded: \`\${CLAUDE_SKILL_DIR}/types/claude-code.d.ts\`, this build's API and built-in tools, written as this skill loaded (this process's own folder: after a restart the next load of this skill writes and names a new one). Once the engine has loaded the mod (from this mods folder, or a \`--plugin-dir\` folder it hot-reloads), \`<mod folder>/.claude-plugin/types/\` holds the same for the editor: \`claude-code/index.d.ts\`, the API; \`claude-code-tools/index.d.ts\`, so \`e.tool === "Bash"\` narrows \`e\`; \`claude-code-mcp/index.d.ts\`, the MCP tools connected when the mod last reloaded; each \`dependencies\` plugin's contract; and a \`tsconfig.json\` the mod's own extends, so \`tsc -p <mod folder>\` type-checks it. The API file carries every event's input and result, every noun and method on \`$\` with its doc comment and an example, and every element's props, in about 14,000 lines: grep it for the name at hand (\`'tool.call'\`, \`Pane: {\`, \`export type ToolCallResult\`).

WHAT HAPPENS WHEN THE TURN ENDS. Loading this skill through the Skill tool or its slash command starts the engine's watch on the folder that holds the mod folders. The first file written under it makes the engine ask the person, once, right then, while the turn goes on: "Turn on the mods Claude writes in this session?", with \`How does this work?\` first, then \`Turn them on\` and \`Not now\`. That question is the switch, and the person alone answers it: no permission mode, rule or hook does. On \`Turn them on\` the folder joins the session's plugin folders and the mod loads when the turn ends, whole, and each later edit reloads it when the turn that made the edit ends. The question stays up until answered. The answer reaches you as a notice at your next turn, which the engine may start for an enabling: enabled, with what the load came to; declined (the mods are written and load the next time this session starts; the person can ask for the question again); still open (dismissed or closed; asked again); or off, with the reason (nobody could be asked, as under \`claude -p\`; the question got no pick three times; an organization's policy; an untrusted workspace). A process that restarted loads an enabled folder again by itself; otherwise its watch starts the next time this skill loads, and a manifest already in the folder raises the question when that turn ends.

A reload runs \`register\` and \`session.start\` again. \`$.state\` (the session's) and \`$.store\` (across sessions) stay; the module's own variables start over. New code meets old values: \`shape\`, in \`reference.md\`.

\${CLAUDE_SESSION_SURFACE}

## A mod in one paragraph

\`on(event, matcher?, hook)\` adds a hook, and every hook is \`($, e, next)\`: \`$\` is the engine interface, each call spelled noun then method; \`e\` is the event's input, a plain frozen value; \`next(e)\` runs the plugins beneath and then the engine's own behaviour, resolving to the event's result. A hook that returns without \`next\` answers for itself; \`next({ ...e, x })\` rewrites what the rest sees. The module has no DOM or Node: \`$\` reaches everything outside it. JSX compiles against the global \`h\`, and the elements come from the drawing surface's own table, \`const { Box, Text, Button } = $.ui.resolve(e)\`, where \`e.surface\` is \`terminal\`, \`desktop\`, \`vscode\` or \`mobile\`.

## From the ask to the shape

When a person asks for a panel, or for anything kept beside the chat, build a pane as a mod, not a page, even if what it shows is fixed. A page is for a document to read or send.

Each example, in \`\${CLAUDE_SKILL_DIR}/examples/\`, is one complete hooks module; with the two JSON files above and any contract, it loads, validates and type-checks on this build.

| The person asks for | What it is | Shown in |
| --- | --- | --- |
| a pane, panel, sidebar, live view | \`$.ui.open({ id, title })\`, drawn by a \`ui.render\` hook on \`{ component: 'Pane', requestId: id }\`; it resolves \`{ isPlaced }\`, whether a surface draws it now | \`pane.tsx\`, its contract \`pane-state.d.ts\` |
| a band or row above the prompt | a \`ui.render\` hook on \`{ component: 'AbovePrompt' }\` returning a tree, or \`next(e)\` with nothing to show | \`band.tsx\`, its contract \`band-state.d.ts\` |
| something on or under a tool call's row | a \`ui.render\` hook on \`{ component: 'ToolUse' }\` with \`await next(e)\` in its tree to keep the row. Mobile apps draw it as one quiet line, or as a card under the row when \`borderStyle\` or \`backgroundColor\` is on the Box that holds the row and your content. Use a card for what a person should see without a tap, such as a chart, a list or a report | its doc in the types |
| a status line entry | \`$.ui.status(text)\` from any hook; \`undefined\` clears it | \`tool-call.ts\` |
| a toast | \`$.ui.toast(text)\` from any hook | \`band.tsx\` |
| block, rewrite or react to a tool call | \`on('tool.call', { tool }, hook)\`: return \`{ deny }\`, call \`next({ ...e, ... })\`, or \`await next(e)\` and act on the result | \`tool-call.ts\` |
| change or react to a prompt | \`on('prompt.submit', hook)\`: \`next({ ...e, text })\` | \`band.tsx\` |
| change the system prompt | \`on('prompt.compose', hook)\`: answer \`next(e)\`'s \`{ sections }\` with one added last (\`scope: 'session'\`), replaced or dropped | its doc in the types |
| play a sound | \`$.audio.play({ asset })\` from any hook, the asset a file of the mod's | its doc in the types |
| a slash command | \`$.command.register({ name, description })\` in \`session.start\`, answered by a \`command.run\` hook returning \`{ text }\` | \`pane.tsx\` |
| values a drawing reads | \`atom(ref, initial)\`, \`read($, atom)\` while drawing, \`update($, atom, fn)\` from a handler or another event; the write redraws the readers; each value declared in the contract | \`pane-state.d.ts\` |
| work on a timer, a tool the model calls, a subagent type, model calls, files, processes | \`$.clock\`, \`$.tool\`, \`$.agent\`, \`$.model\`, \`$.fs\`, \`$.process\` | \`\${CLAUDE_SKILL_DIR}/reference.md\` |

## Checking it and reading what the engine refused

\`claude plugin validate <mod folder>\` reads the manifest and the module's source the way the engine will, and reports what the module hooks and calls and all the engine would refuse. Type-check the mod: with its types laid, \`tsc -p <mod folder>\`; else (the first write, \`claude -p\`, an SDK host), with the \`tsconfig.json\` from the types file's header, kept outside the mod folder, its \`include\` naming that file and the mod's \`hooks\`. Test what was asked in a \`*.test.ts\` like the example \`pane.test.tsx\`, seeding what an earlier version stored: run \`claude plugin test <mod folder>\`. A finished mod is at its full path, loaded or not by the hot-reloading answer: enabled, it is loaded when the turn ends, with nothing to run; any other answer, it is not loaded.

While the session hot-reloads a plugin folder the transcript carries one dim line naming the plugin, the event and the reason when a hook fails or a module does not load, and a hook whose tree does not validate is such a hook, skipped alone: \`<plugin>: ui.render hook skipped: returned the wrong shape (a tree <Component> refuses: <reason>)\`. A failed hook of a mod you wrote comes back to you as a notice at your next turn. In any other session those lines go to the debug log alone, as \`<plugin>: <line>\`. The debug log (\`claude --debug\`) carries a line for every occurrence and every result the engine refused.

\`\${CLAUDE_SKILL_DIR}/reference.md\` is the long form: the full event list, streaming events, \`ui.render\` in depth, \`$.state\` contracts, \`--plugin-dir\` and \`CLAUDE_CODE_PLUGIN_DIRS\` while developing, \`userConfig\` options, what a test holds, and Sharing a mod, the GitHub road, done when the person asks, or says yes where this skill offers it: \`.claude-plugin/marketplace.json\` in its repository and, in the README, \`/plugin install <mod> --marketplace <owner>/<repo>\`.
