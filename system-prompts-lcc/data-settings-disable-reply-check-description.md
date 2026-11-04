<!--
name: 'Data: disableReplyCheck setting description'
description: >-
  Description of the `disableReplyCheck` setting in Claude Code's settings JSON
  schema. The model reads it through /update-config and settings validation
  errors; it is also shown to users in the settings help.
ccVersion: 2.1.318
-->
Disable the reply check in Claude Tag sessions on a self-hosted runner. The check re-prompts Claude, at most four times a turn, when a turn ends without a call to one of Claude Tag's reply tools. It is not a hook, so disableAllHooks does not affect it. Disabling it also stops two messages to Claude that Anthropic's service can request for such a session: a nudge after a long stretch of work with no visible update, and a reminder added to prompts. Claude Code's built-in reminder to give progress updates, on models that have it, is then no longer held back. Set it in managed settings; false there keeps the check on. Everywhere else it is ignored and the check stays on. Has no effect on sessions that Anthropic hosts.
