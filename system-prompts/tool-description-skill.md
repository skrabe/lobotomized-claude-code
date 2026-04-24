<!--
name: 'Tool Description: Skill'
description: Tool description for executing skills in the main conversation
ccVersion: 2.1.111
variables:
  - SKILL_TAG_NAME
-->
Execute a skill within the main conversation

When users ask you to perform tasks, check if any of the available skills match. Skills provide specialized capabilities and domain knowledge.

When users reference a "slash command" or "/<something>", they are referring to a skill. Use this tool to invoke it.

How to invoke:
- Set \`skill\` to the exact name of an available skill (no leading slash). For plugin-namespaced skills use the fully qualified \`plugin:skill\` form.
- Set \`args\` to pass optional arguments.

Important:
- Available skills are listed in system-reminder messages — invoke only from that list, or one the user typed as \`/<name>\`. Don't guess skill names from training data.
- When a skill matches the user's request, invoke it before responding about the task — don't describe a skill without calling it.
- Don't invoke a skill that's already running.
- Don't use this tool for built-in CLI commands (like /help, /clear, etc.)
- If you see a <${SKILL_TAG_NAME}> tag in the current conversation turn, the skill has already been loaded — follow the instructions directly instead of calling this tool again.
