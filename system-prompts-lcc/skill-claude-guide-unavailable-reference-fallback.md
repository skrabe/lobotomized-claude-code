<!--
name: 'Skill: Claude guide unavailable reference fallback'
description: >-
  Provides the Claude guide skill with an embedded live-sources reference and
  fallback instructions when its reference files cannot be written to disk
ccVersion: 2.1.234
variables:
  - RENDER_SKILL_TEMPLATE_FN
  - CLAUDE_GUIDE_SKILL_DATA
-->
## Reference Files Unavailable

This skill's reference files could not be written to disk for this session, so the \`{lang}/…\`, \`shared/…\`, and \`curl/…\` files cited above cannot be Read. Do not guess their contents — WebFetch the matching URL from \`shared/live-sources.md\`, included below, whenever the Reading Guide points at one of those files. If a cited \`shared/…\` file has no matching URL below (skill-authored guides such as \`shared/prompt-audit.md\`, \`shared/agent-design.md\`, \`shared/platform-availability.md\`), state that the reference is unavailable this session and proceed best-effort from this document.

<doc path="shared/live-sources.md">
${RENDER_SKILL_TEMPLATE_FN(CLAUDE_GUIDE_SKILL_DATA.SKILL_FILES["shared/live-sources.md"]??"",CLAUDE_GUIDE_SKILL_DATA.SKILL_MODEL_VARS).trim()}
</doc>
