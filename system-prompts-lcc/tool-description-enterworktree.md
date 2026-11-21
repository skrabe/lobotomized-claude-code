<!--
name: 'Tool Description: EnterWorktree'
description: Tool description for the EnterWorktree tool.
ccVersion: 2.1.330
variables:
  - IS_WORKING_COPY_ISOLATION
  - IS_MODULE_ISOLATION
-->

Create an isolated ${IS_WORKING_COPY_ISOLATION?"working copy":"git worktree"} and switch the session into it. Use only when explicitly instructed to work in a worktree — either the user says "worktree" (start/create/use a worktree) or CLAUDE.md / memory directs it. For branch switching, use ${IS_WORKING_COPY_ISOLATION?"version control":"git"} commands instead; for feature/bugfix work, use ${IS_WORKING_COPY_ISOLATION?"the normal":"normal git"} workflow.

## Requirements

${IS_WORKING_COPY_ISOLATION?"":`- ${IS_MODULE_ISOLATION?"To create a new worktree, must":"Must"} be in a git repository, OR have WorktreeCreate/WorktreeRemove hooks configured in settings.json
`}- Creating a new worktree (\`name\`) requires not already being in one; switching to an existing worktree (\`path\`) works from anywhere, including from within another worktree.

## Behavior

${IS_WORKING_COPY_ISOLATION?"- Creates a working copy with the project's version control; the result gives its path. What it starts from is governed by the `worktree.baseRef` setting: `fresh` (default) is the latest mainline; `head` is what the current directory has now":"- In a git repo: creates a new worktree under `.claude/worktrees/` on a new branch. The base ref follows the `worktree.baseRef` setting: `fresh` (default) branches from origin/<default-branch>; `head` branches from current local HEAD.\n- Outside a git repo: delegates to the WorktreeCreate/WorktreeRemove hooks."}
- Switches the session's working directory to the new worktree. Use ExitWorktree to leave mid-session; on session exit while still inside, the user is prompted to keep or remove it.
- ${IS_MODULE_ISOLATION?"The `path` must be a working copy that the project's version control lists for the current repository, or, on first entry from the launch directory of a multi-repo workspace, a git worktree of a repository nested inside it; any other is rejected.":`On first entry from the launch directory, a ${IS_WORKING_COPY_ISOLATION?"git ":""}worktree \`path\` must appear in \`git worktree list\` for the current repository or a repository nested inside the multi-repository workspace; paths registered by neither are rejected.`}
- When switching with \`path\` from an active worktree, ${IS_MODULE_ISOLATION?"a git worktree must lie":"the target must be"} under \`.claude/worktrees/\` of the same repository. The previous worktree remains on disk untouched, and only the new worktree is tracked for exit-time cleanup.
- When switching from a pinned agent, ${IS_MODULE_ISOLATION?"a git worktree must lie":"the target must be"} under \`.claude/worktrees/\` of the same repository. The switch affects only that agent, not the parent session.
- After another switch, previously visited worktrees are no longer writable. Re-issue EnterWorktree with \`path\` before writing in one again.

## Parameters

- \`name\` (optional): name for a new worktree; random if neither \`name\` nor \`path\` is given.
- \`path\` (optional): path to an existing worktree to enter instead of creating one — must be a registered worktree. Mutually exclusive with \`name\`. ExitWorktree won't remove a worktree entered this way; use \`action: "keep"\` to return to the original directory.
