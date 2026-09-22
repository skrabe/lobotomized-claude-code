<!--
name: 'Tool Description: ExitWorktree'
description: 'Roughly, the reverse of the ExitWorktree'
ccVersion: 2.1.72
-->
Exit a worktree session created by EnterWorktree this session and return to the original working directory. It operates only on worktrees EnterWorktree created in this session — not ones you made with \`git worktree add\`, ones from a previous session, or the current directory if EnterWorktree was never called. Called outside an EnterWorktree session it's a no-op: it reports no active worktree session and changes nothing.

Call only when the user asks to exit/leave/end the worktree session; don't call it proactively.

## Parameters

- \`action\` (required): \`"keep"\` leaves the worktree directory and branch intact (use to return later or preserve changes); \`"remove"\` deletes the worktree directory and its branch (use for a clean exit when work is done or abandoned).
- \`discard_changes\` (optional, default false): only meaningful with \`action: "remove"\`. If the worktree has uncommitted files or commits not on the original branch, removal is refused unless this is \`true\`. When the tool returns an error listing changes, confirm with the user before re-invoking with \`discard_changes: true\`.

## Behavior

Restores the session's working directory to where it was before EnterWorktree and clears CWD-dependent caches (system prompt sections, memory files, plans directory). An attached tmux session is killed on \`remove\`, left running on \`keep\` (its name is returned so the user can reattach). After exiting, EnterWorktree can be called again for a fresh worktree.
