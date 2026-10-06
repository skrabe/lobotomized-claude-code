<!--
name: 'Tool result: skill requires Git Bash'
description: >-
  Error returned when a skill with shell: bash frontmatter is invoked on Windows
  without Git Bash
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_SKILL_REQUIRES_GIT_BASH_VAR_0
-->
Skill ${TOOL_RESULT_SKILL_REQUIRES_GIT_BASH_VAR_0} requires bash (\`shell: bash\` in frontmatter) but Git Bash was not found. Install Git for Windows (https://git-scm.com/downloads/win), or change the skill's frontmatter to \`shell: powershell\`.
