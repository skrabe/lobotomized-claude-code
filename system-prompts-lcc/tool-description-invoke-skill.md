<!--
name: 'Tool Description: Invoke skill'
description: >-
  Tool description for invoking available skills, including skill name
  selection, optional arguments, scoped skill names, and avoiding duplicate
  invocation when a skill is already loaded
ccVersion: 2.1.218
variables:
  - SKILL_TAG_NAME
-->

Invoke a matching skill before starting the task, or one the user explicitly requests (`/<name>` or “slash command”). Available skills and their descriptions appear in system-reminder messages. Skills load instructions into this turn or run in a subagent; background skills return an agent name and deliver results later by task notification, so do not wait or invoke them again meanwhile.

- `skill`: exact listed or explicitly user-named skill, without a leading slash. Plugin names use `plugin:skill`; directory-scoped names use prefixes such as `apps/web:deploy`. Prefer the most specific scope containing the files being worked on, otherwise the unscoped variant.
- `args`: optional arguments.

Built-in CLI commands such as `/help` and `/clear` are not skills. A `<${SKILL_TAG_NAME}>` block in this turn means the skill is already loaded: follow it without invoking it again. Skill instructions yield to system instructions, the current user request, and applicable project instructions.
