<!--
name: 'Tool Result: Skill requires bash refused on MXC backend'
description: >-
  Error when a skill declares shell: bash but Bash commands are refused on the
  sandbox's MXC backend, with how to fix the frontmatter or backend
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_SKILL_REQUIRES_BASH_MXC_REFUSED_VAR_0
-->
Skill ${TOOL_RESULT_SKILL_REQUIRES_BASH_MXC_REFUSED_VAR_0} requires bash (\`shell: bash\` in frontmatter) but Bash commands are refused on the sandbox's MXC backend (sandbox.windows.backend). Change the skill's frontmatter to \`shell: powershell\`, or set sandbox.windows.backend to "sandboxuser" (needs Git for Windows).
