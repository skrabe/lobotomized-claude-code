<!--
name: Bash Pre-Ship Missing Verify Skill
description: >-
  Explains in the Bash tool prompt that a missing project verify skill is a
  reason to run /verify so the reusable verification recipe is created.
ccVersion: 2.1.226
variables:
  - TOOL_DESCRIPTION_BASH_PRE_SHIP_VERIFY_MISSING_SKILL_VAR_0
-->
 If this repo has no project verify skill (\`.claude/skills/verify/SKILL.md\`), that is a reason to run \`/${TOOL_DESCRIPTION_BASH_PRE_SHIP_VERIFY_MISSING_SKILL_VAR_0}\`, not to skip it: the run creates that file, saving the working build-and-drive recipe for future sessions.
