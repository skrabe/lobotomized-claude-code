<!--
name: 'Tool Description: SendMessageTool'
description: Agent teams version of SendMessageTool.
ccVersion: 2.1.224
-->

# SendMessage

Send a message to another agent by teammate name, or to `"main"` for the main conversation (background subagents only):

```json
{"to": "researcher", "summary": "assign task 1", "message": "start on task #1"}
```

Plain text output is not visible to teammates. Refer to agents by name — names keep working after an agent completes (a send resumes it from its transcript). Use the raw `agentId` (format `a...-...`) from its spawn result only when the agent has no name, or when a newer agent took the name (latest wins). Messages are delivered automatically, so don't poll an inbox.${CROSS_SESSION_SECTION}
