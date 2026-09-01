<!--
name: 'Tool Description: EnterWorktree'
description: Tool description for the EnterWorktree tool.
ccVersion: 2.1.204
-->

Create an isolated git worktree and switch the session into it. Use only when explicitly instructed to work in a worktree — either the user says "worktree" (start/create/use a worktree) or CLAUDE.md / memory directs it. For branch switching or normal feature/bugfix work, use git commands instead.

Requirements: be in a git repository, or have WorktreeCreate/WorktreeRemove hooks configured in settings.json. Creating a new worktree (\`name\`) requires not already being in one; switching to an existing worktree (\`path\`) works from anywhere, including from within another worktree.

## Behavior

- In a git repo: creates a new worktree under \`.claude/worktrees/\` on a new branch. The base ref follows the \`worktree.baseRef\` setting: \`fresh\` (default) branches from origin/<default-branch>; \`head\` branches from current local HEAD.
- Outside a git repo: delegates to the WorktreeCreate/WorktreeRemove hooks.
- Switches the session's working directory to the new worktree. Use ExitWorktree to leave mid-session; on session exit while still inside, the user is prompted to keep or remove it.
- On first entry from the launch directory, \`path\` must appear in \`git worktree list\` for the repository that owns it: either the current repository or, in a multi-repo workspace, a repository nested inside it. Paths registered by neither are rejected.
- When switching via \`path\` from an existing worktree or an agent whose working directory was pinned at launch, the target must be under \`.claude/worktrees/\` of the same repository. From a pinned agent, the switch affects only that agent, not the parent session.
- After a further switch, previously visited worktrees are no longer writable; re-issue EnterWorktree with \`path\` to return to one.

## Parameters

- \`name\` (optional): name for a new worktree; random if neither \`name\` nor \`path\` is given.
- \`path\` (optional): path to an existing worktree to enter instead of creating one — must be a registered worktree (appears in \`git worktree list\`). Mutually exclusive with \`name\`. ExitWorktree won't remove a worktree entered this way; use \`action: "keep"\` to return to the original directory.
