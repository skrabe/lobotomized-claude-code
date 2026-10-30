<!--
name: 'Data: blockWritesOutsideWorkingDirectories setting'
description: >-
  Describes the file-tool write boundary, session-file exceptions, settings-file
  protection and worktree-tool restrictions without claiming to constrain shell
  or MCP execution
ccVersion: 2.1.314
-->
Refuse file-tool writes (Write, Edit, NotebookEdit) outside the working directories in every permission mode; true in any settings source wins. No allow rule lifts it. Files that Claude Code keeps for the session are not refused: its plan files, scratchpad and background job folder, and the auto-memory of this project, unless the CLAUDE_COWORK_MEMORY_PATH_OVERRIDE environment variable or a repository settings file points it elsewhere. Nothing runs them unless the model asks. Also refuses file-tool writes to Claude Code settings files, inside the working directories too, and takes EnterWorktree and ExitWorktree, which move the working directory, out of the tools on offer. Does not limit shell commands, MCP tools, the programs that hooks run, or the memory tools. Cloud sessions (Claude Code on the web), whose file tools run in a container that is itself the boundary, may not apply it.
