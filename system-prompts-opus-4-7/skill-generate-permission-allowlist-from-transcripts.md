<!--
name: 'Skill: Generate permission allowlist from transcripts'
description: >-
  Analyzes session transcripts to extract frequently used read-only tool-call
  patterns and adds them to the project's .claude/settings.json permission
  allowlist to reduce permission prompts
ccVersion: 2.1.167
-->
# Fewer Permission Prompts

Look through my transcripts' MCP and bash tool calls and make a prioritized list of patterns to add to my permission allowlist to reduce permission prompts. Focus on read-only commands.

The permission format is: \`Bash(foo*)\`, \`Bash(foo)\`, \`Bash(foo bar *)\`, \`mcp__slack__slack_read_thread\`, etc.

Then add these to the project \`.claude/settings.json\` under \`permissions.allow\`.

## Steps

1. **Locate transcripts.** Session transcripts live at \`~/.claude/projects/<sanitized-cwd>/*.jsonl\`. Each line is a JSON object. Tool calls appear as \`assistant\` messages with \`message.content[]\` entries of \`type: "tool_use"\`. The \`name\` field identifies the tool (e.g. \`"Bash"\`, \`"mcp__slack__slack_read_thread"\`); for Bash, \`input.command\` is the shell string.

   Scan recent transcripts across the user's projects dir — not just the current project — so the allowlist reflects actual usage. Cap the scan at ~50 most-recently-modified JSONL files to stay fast.

2. **Extract tool-call frequencies.**
   - For \`Bash\` calls: parse \`input.command\`, take the leading command token (handling \`sudo\`, \`timeout\`, pipes, \`&&\`, env-var prefixes). Record the command + first subcommand pair (e.g. \`git status\`, \`gh pr view\`, \`ls\`, \`cat\`).
   - For MCP calls: record the full tool name (e.g. \`mcp__slack__slack_read_thread\`).
   - Count occurrences across the scanned transcripts.

3. **Filter to read-only.** Keep only commands that don't mutate state. Read-only examples: \`ls\`, \`cat\`, \`pwd\`, \`git status\`, \`git log\`, \`git diff\`, \`git show\`, \`git branch\`, \`rg\`, \`grep\`, \`find\`, \`head\`, \`tail\`, \`wc\`, \`file\`, \`which\`, \`echo\`, \`date\`, \`gh pr view\`, \`gh pr list\`, \`gh pr diff\`, \`gh issue view\`, \`gh issue list\`, \`gh run list\`, \`gh run view\`, \`gh api\` (GET), \`bun run typecheck\`, \`bun run lint\`, \`bun run test\` (non-mutating), \`docker ps\`, \`docker logs\`, \`kubectl get\`, \`kubectl describe\`, \`ps\`, \`top\`, \`df\`, \`du\`, \`env\`, \`printenv\`, any MCP tool with \`read\`/\`get\`/\`list\`/\`search\`/\`view\` in its name.

   Drop anything that writes, deletes, renames, pushes, merges, installs, or runs a build/test with side effects. When in doubt, leave it out.

   **Never allowlist a pattern that grants arbitrary code execution.** A wildcard rule for any of these (e.g. \`Bash(python3:*)\`) is equivalent to allowing arbitrary code execution. This list is not exhaustive — apply the same rule to anything in the same category:
   - Interpreters: \`python\`/\`python3\`, \`node\`, \`bun\`, \`deno\`, \`ruby\`, \`perl\`, \`php\`, \`lua\`, etc.
   - Shells: \`bash\`, \`sh\`, \`zsh\`, \`fish\`, \`eval\`, \`exec\`, \`ssh\`, etc.
   - Package runners: \`npx\`, \`bunx\`, \`uvx\`, \`uv run\`, etc.
   - Task-runner wildcards: \`npm run *\`, \`yarn run *\`, \`pnpm run *\`, \`bun run *\`, \`make *\`, \`just *\`, \`cargo run *\`, \`go run *\`, etc. — an exact \`Bash(bun run typecheck)\` is fine, \`Bash(bun run *)\` is not
   - \`gh api *\`, \`docker run\`/\`exec\`, \`kubectl exec\`, \`sudo\`, and similar

4. **Drop commands Claude Code already auto-allows.** These never prompt and need no allowlist entry. If you see them in transcripts, skip them; don't suggest them.

   - **Always auto-allowed (any args):** \`cal\`, \`uptime\`, \`cat\`, \`head\`, \`tail\`, \`wc\`, \`stat\`, \`strings\`, \`hexdump\`, \`od\`, \`nl\`, \`id\`, \`uname\`, \`free\`, \`df\`, \`du\`, \`locale\`, \`groups\`, \`nproc\`, \`basename\`, \`dirname\`, \`realpath\`, \`cut\`, \`paste\`, \`tr\`, \`column\`, \`tac\`, \`rev\`, \`fold\`, \`expand\`, \`unexpand\`, \`fmt\`, \`comm\`, \`cmp\`, \`numfmt\`, \`readlink\`, \`diff\`, \`true\`, \`false\`, \`sleep\`, \`which\`, \`type\`, \`expr\`, \`test\`, \`getconf\`, \`seq\`, \`tsort\`, \`pr\`, \`echo\`, \`printf\`, \`ls\`, \`cd\`, \`find\`.
   - **Auto-allowed with zero args only:** \`pwd\`, \`whoami\`, \`alias\`.
   - **Auto-allowed exact forms:** \`claude -h\`, \`claude --help\`, \`node -v\`, \`node --version\`, \`python --version\`, \`python3 --version\`, \`ip addr\`.
   - **Auto-allowed with safe flags only (validated):** \`xargs\`, \`file\`, \`sed\` (read-only expressions), \`sort\`, \`man\`, \`help\`, \`netstat\`, \`ps\`, \`base64\`, \`grep\`, \`egrep\`, \`fgrep\`, \`sha256sum\`, \`sha1sum\`, \`md5sum\`, \`tree\`, \`date\`, \`hostname\`, \`info\`, \`lsof\`, \`pgrep\`, \`tput\`, \`ss\`, \`fd\`, \`fdfind\`, \`aki\`, \`rg\`, \`jq\`, \`uniq\`, \`history\`, \`arch\`, \`ifconfig\`, \`pyright\`.
   - **All git read-only subcommands:** \`git status\`, \`git log\`, \`git diff\`, \`git show\`, \`git blame\`, \`git branch\`, \`git tag\`, \`git remote\`, \`git ls-files\`, \`git ls-remote\`, \`git config --get\`, \`git rev-parse\`, \`git describe\`, \`git stash list\`, \`git reflog\`, \`git shortlog\`, \`git cat-file\`, \`git for-each-ref\`, \`git worktree list\`, etc.
   - **All gh read-only subcommands:** \`gh pr view\`, \`gh pr list\`, \`gh pr diff\`, \`gh pr checks\`, \`gh pr status\`, \`gh issue view\`, \`gh issue list\`, \`gh issue status\`, \`gh run view\`, \`gh run list\`, \`gh workflow list\`, \`gh workflow view\`, \`gh repo view\`, \`gh release view\`, \`gh release list\`, \`gh api\` (GET), \`gh auth status\`, etc.
   - **Docker read-only subcommands:** \`docker ps\`, \`docker images\`, \`docker logs\`, \`docker inspect\`.

   Source of truth: \`src/tools/BashTool/readOnlyValidation.ts\` (\`READONLY_COMMANDS\`, \`READONLY_NOARGS\`, \`READONLY_EXACT\`, \`COMMAND_ALLOWLIST\`) and \`src/utils/shell/readOnlyCommandValidation.ts\` (\`GIT_READ_ONLY_COMMANDS\`, \`GH_READ_ONLY_COMMANDS\`, \`DOCKER_READ_ONLY_COMMANDS\`, \`RIPGREP_READ_ONLY_COMMANDS\`, \`PYRIGHT_READ_ONLY_COMMANDS\`). If you're in this repo and unsure whether a command is covered, grep these files rather than guessing.

5. **Pick the pattern form.** Use the narrowest pattern that covers the observed usage:
   - Many variants (\`git log\`, \`git log --oneline\`, \`git log main..HEAD\`) → \`Bash(git log *)\` — note the space before \`*\`, required for prefix matching.
   - A single common exact invocation → \`Bash(foo)\` with no wildcard.
   - MCP → the full tool name verbatim (no wildcard needed).
   - Never widen a pattern to where it conflicts with the rules above (no arbitrary code execution, no mutation/side effects).

6. **Prioritize.** Rank by count descending. Drop anything seen fewer than ~3 times. Cap at the top ~20 so the user can skim.

7. **Present the prioritized list** as a markdown table with columns: rank, pattern, count, one-line description. Example:

   | # | Pattern | Count | Notes |
   |---|---------|-------|-------|
   | 1 | \`Bash(git status *)\` | 142 | repo status checks |
   | 2 | \`Bash(gh pr view *)\` | 87 | PR inspection |
   | 3 | \`mcp__slack__slack_read_thread\` | 54 | Slack thread reads |

8. **Merge into \`.claude/settings.json\`** in the current project (not \`~/.claude/settings.json\`, not \`.claude/settings.local.json\`). Create the file if it doesn't exist. Preserve existing keys and existing \`permissions.allow\` entries; de-duplicate against what's there; don't remove anything; don't reorder unrelated fields.

9. **Report back.** Tell the user what you added (count + a few examples), what was already in the allowlist, and what you skipped and why (e.g. "dropped \`rm\` and \`git push\` — not read-only; dropped \`cat\`/\`ls\`/\`git status\` — already auto-allowed").

Do not add anything to \`permissions.deny\` or \`permissions.ask\`. Do not touch any other settings field.
