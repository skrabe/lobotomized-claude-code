<!--
name: 'Skill: Claude guide detected language readme'
description: >-
  Detected-Language section of the Claude API guide skill that inlines the
  language's claude-api/README.md as a <doc> block
ccVersion: 2.1.234
variables:
  - SKILL_CLAUDE_GUIDE_DETECTED_LANGUAGE_README_VAR_0
  - SKILL_CLAUDE_GUIDE_DETECTED_LANGUAGE_README_VAR_1
  - SKILL_CLAUDE_GUIDE_DETECTED_LANGUAGE_README_VAR_2
  - SKILL_CLAUDE_GUIDE_DETECTED_LANGUAGE_README_VAR_3
  - SKILL_CLAUDE_GUIDE_DETECTED_LANGUAGE_README_VAR_4
  - SKILL_CLAUDE_GUIDE_DETECTED_LANGUAGE_README_VAR_5
-->
## Detected Language: ${SKILL_CLAUDE_GUIDE_DETECTED_LANGUAGE_README_VAR_0}

\`${SKILL_CLAUDE_GUIDE_DETECTED_LANGUAGE_README_VAR_1}\` is included below since every task starts there.${SKILL_CLAUDE_GUIDE_DETECTED_LANGUAGE_README_VAR_2?" Read the other referenced files from the base directory on demand. That directory is session-scoped — after resuming a session, or if a Read under it ever fails, re-invoke this skill to re-extract.":""}

<doc path="${SKILL_CLAUDE_GUIDE_DETECTED_LANGUAGE_README_VAR_1}">
${SKILL_CLAUDE_GUIDE_DETECTED_LANGUAGE_README_VAR_3(SKILL_CLAUDE_GUIDE_DETECTED_LANGUAGE_README_VAR_4,SKILL_CLAUDE_GUIDE_DETECTED_LANGUAGE_README_VAR_5.SKILL_MODEL_VARS).trim()}
</doc>
