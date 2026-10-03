<!--
name: 'Tool Result: ProposeSkills SKILL.md shown for rewrite'
description: >-
  Shows Claude the current SKILL.md (line-numbered) of a skill it proposed to
  change, since a saved proposal replaces the whole file, and tells it to call
  again with a complete SKILL.md or choose another approach
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_PROPOSESKILLS_SKILL_MD_SHOWN_FOR_REWRITE_VAR_0
  - TOOL_RESULT_PROPOSESKILLS_SKILL_MD_SHOWN_FOR_REWRITE_VAR_1
  - TOOL_RESULT_PROPOSESKILLS_SKILL_MD_SHOWN_FOR_REWRITE_VAR_2
-->
${TOOL_RESULT_PROPOSESKILLS_SKILL_MD_SHOWN_FOR_REWRITE_VAR_0} is not in this conversation. A saved proposal replaces the whole file, so here it is, each line after its number and a tab, which are not part of the file; call again with a complete SKILL.md that keeps everything worth keeping, or ${TOOL_RESULT_PROPOSESKILLS_SKILL_MD_SHOWN_FOR_REWRITE_VAR_1}.${TOOL_RESULT_PROPOSESKILLS_SKILL_MD_SHOWN_FOR_REWRITE_VAR_2}
