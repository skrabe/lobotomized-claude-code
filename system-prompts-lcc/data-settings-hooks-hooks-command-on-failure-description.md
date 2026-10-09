<!--
name: 'Data: hooks.hooks.(command).onFailure setting description'
description: >-
  Description of the `hooks.hooks.(command).onFailure` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.295
-->
What a failure of this hook does: it could not start (a missing script or plugin directory), timed out, exited with a code other than 0 or 2, or printed JSON that is invalid or fails validation. 'continue' (default): the failure is reported and the action goes ahead. 'block': the failure counts as exit code 2, so the action the event guards (a tool call, a permission request, a prompt) is blocked. Ignored for async hooks and on Stop, SubagentStop, TaskCompleted and TeammateIdle.
