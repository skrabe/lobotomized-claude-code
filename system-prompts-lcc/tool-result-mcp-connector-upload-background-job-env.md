<!--
name: 'Tool result: MCP connector upload background job environment'
description: >-
  Explains a connector file send is refused because the session environment
  carries background-job marks, and how the user can start a clean terminal
ccVersion: 2.1.319
-->
sending a file to a connector needs the user to allow it when Claude Code asks at its own prompt in a terminal, and this session's environment marks it as a background job or as started inside one (for example, with claude --bg), where another program may answer that prompt, so an Allow given there does not count. To send a file, the user would at least have to start Claude Code in a terminal whose environment does not carry a background job's marks. A terminal can carry them without being inside a job: for example, a window of a tmux server started inside such a job, or a shell whose own start-up files set them
