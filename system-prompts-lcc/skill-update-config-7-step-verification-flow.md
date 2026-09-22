<!--
name: 'Skill: update-config (7-step verification flow)'
description: >-
  A skill that guides Claude through a 7-step process to construct and verify
  hooks for Claude Code, ensuring they work correctly in the user's specific
  project environment.
ccVersion: 2.1.77
-->
## Constructing a Hook (with verification)

Given an event, matcher, target file, and desired behavior, follow this flow. Each step catches a different failure class — a hook that silently does nothing is worse than no hook.

1. **Dedup.** Read the target file. If a hook already exists on the same event+matcher, show the existing command and ask: keep, replace, or add alongside.

2. **Construct the command for THIS project.** The hook receives JSON on stdin. Build a command that:
   - Extracts payload safely — `jq -r` into a quoted variable, or `{ read -r f; ... "$f"; }`; not unquoted `| xargs` (splits on spaces).
   - Invokes the tool the way this project runs it (npx/bunx/yarn/pnpm? Makefile target? globally installed?).
   - Skips inputs the tool can't handle (`--ignore-unknown`, or guard by extension).
   - Stays raw for now — no `|| true`, no stderr suppression. Wrap it after the pipe-test passes.

3. **Pipe-test the raw command.** Synthesize the stdin payload and pipe it:
   - `Pre|PostToolUse` on `Write|Edit`: `echo '{"tool_name":"Edit","tool_input":{"file_path":"<a real file from this repo>"}}' | <cmd>`
   - `Pre|PostToolUse` on `Bash`: `echo '{"tool_name":"Bash","tool_input":{"command":"ls"}}' | <cmd>`
   - `Stop`/`UserPromptSubmit`/`SessionStart`: most don't read stdin, so `echo '{}' | <cmd>` suffices.

   Check exit code AND side effect (file actually formatted, test actually ran). On failure you get a real error — fix (wrong package manager? tool not installed? jq path wrong?) and retest. Once it works, wrap with `2>/dev/null || true` (unless the user wants a blocking check).

4. **Write the JSON.** Merge into the target file. If this first-creates `.claude/settings.local.json`, add it to .gitignore — the Write tool doesn't auto-gitignore it.

5. **Validate syntax + schema in one shot:**

   `jq -e '.hooks.<event>[] | select(.matcher == "<matcher>") | .hooks[] | select(.type == "command") | .command' <target-file>`

   Exit 0 + prints your command = correct. Exit 4 = matcher doesn't match. Exit 5 = malformed JSON or wrong nesting. A broken settings.json silently disables ALL settings in that file — fix any pre-existing malformation too.

6. **Prove the hook fires** — only for `Pre|PostToolUse` on a matcher you can trigger in-turn (`Write|Edit` via Edit, `Bash` via Bash). `Stop`/`UserPromptSubmit`/`SessionStart` fire outside this turn — skip to step 7.

   Formatter on `PostToolUse`/`Write|Edit`: introduce a detectable violation via Edit (two blank lines, bad indentation, a missing semicolon — something this formatter corrects; NOT trailing whitespace, Edit strips that before writing), re-read, confirm the hook fixed it. Anything else: temporarily prefix the command in settings.json with `echo "$(date) hook fired" >> /tmp/claude-hook-check.txt; `, trigger the matching tool, read the sentinel.

   Clean up afterward — revert the violation, strip the sentinel prefix — pass or fail.

   If proof fails but pipe-test and `jq -e` passed: the settings watcher only watches directories that had a settings file when this session started. The hook is correct; tell the user to open `/hooks` once (reloads config) or restart. You can't do this yourself — `/hooks` is a user UI menu and opening it ends the turn.

7. **Handoff.** Tell the user the hook is live (or needs `/hooks`/restart per the watcher caveat), and that `/hooks` lets them review, edit, or disable it. The UI only shows "Ran N hooks" if a hook errors or is slow — silent success is invisible by design.
