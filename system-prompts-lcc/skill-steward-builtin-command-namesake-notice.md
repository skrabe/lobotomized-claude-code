<!--
name: 'Skill: Steward built-in command namesake notice'
description: >-
  Explains that nothing started because a custom or other command shares the
  built-in name, what the built-in does, and to type the line again to run it.
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_BUILTIN_COMMAND_NAMESAKE_NOTICE_VAR_0
  - SKILL_STEWARD_BUILTIN_COMMAND_NAMESAKE_NOTICE_VAR_1
  - SKILL_STEWARD_BUILTIN_COMMAND_NAMESAKE_NOTICE_VAR_2
  - SKILL_STEWARD_BUILTIN_COMMAND_NAMESAKE_NOTICE_VAR_3
  - SKILL_STEWARD_BUILTIN_COMMAND_NAMESAKE_NOTICE_VAR_4
  - SKILL_STEWARD_BUILTIN_COMMAND_NAMESAKE_NOTICE_VAR_5
-->
Nothing started. ${SKILL_STEWARD_BUILTIN_COMMAND_NAMESAKE_NOTICE_VAR_0!==void 0?`A custom /${SKILL_STEWARD_BUILTIN_COMMAND_NAMESAKE_NOTICE_VAR_0} isn't loaded, because Claude Code has a built-in command of that name. To use the custom one, rename it, then restart Claude Code.`:`${SKILL_STEWARD_BUILTIN_COMMAND_NAMESAKE_NOTICE_VAR_1} is a command built into Claude Code. ${SKILL_STEWARD_BUILTIN_COMMAND_NAMESAKE_NOTICE_VAR_2(SKILL_STEWARD_BUILTIN_COMMAND_NAMESAKE_NOTICE_VAR_3.length,"Another command here has","Other commands here have")} that name too: ${SKILL_STEWARD_BUILTIN_COMMAND_NAMESAKE_NOTICE_VAR_4.length===0?`type / to find ${SKILL_STEWARD_BUILTIN_COMMAND_NAMESAKE_NOTICE_VAR_2(SKILL_STEWARD_BUILTIN_COMMAND_NAMESAKE_NOTICE_VAR_3.length,"it in the menu, under a longer name","them in the menu, under longer names")}`:`to run ${SKILL_STEWARD_BUILTIN_COMMAND_NAMESAKE_NOTICE_VAR_2(SKILL_STEWARD_BUILTIN_COMMAND_NAMESAKE_NOTICE_VAR_3.length,"that one","one of those")}, type ${SKILL_STEWARD_BUILTIN_COMMAND_NAMESAKE_NOTICE_VAR_4.join(" or ")}`}.`} The built-in ${SKILL_STEWARD_BUILTIN_COMMAND_NAMESAKE_NOTICE_VAR_1} ${SKILL_STEWARD_BUILTIN_COMMAND_NAMESAKE_NOTICE_VAR_5?"commits and pushes your work and opens a pull request as you, if there is none yet, then reviews it and watches it":"watches your open pull request and pushes fixes to it as you"}. To run it, type the same line again.
