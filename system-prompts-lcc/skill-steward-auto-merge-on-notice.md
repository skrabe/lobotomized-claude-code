<!--
name: 'Skill: Steward auto-merge on notice'
description: Notes auto-merge is on for the pull request and how to disable it
ccVersion: 2.1.330
variables:
  - SKILL_STEWARD_AUTO_MERGE_ON_NOTICE_VAR_0
  - SKILL_STEWARD_AUTO_MERGE_ON_NOTICE_VAR_1
-->
${SKILL_STEWARD_AUTO_MERGE_ON_NOTICE_VAR_0?`Auto-merge was turned on for pull request #${SKILL_STEWARD_AUTO_MERGE_ON_NOTICE_VAR_1} after I started watching`:`Auto-merge is on for pull request #${SKILL_STEWARD_AUTO_MERGE_ON_NOTICE_VAR_1}`}. GitHub merges it once its checks and reviews allow, and what I do${SKILL_STEWARD_AUTO_MERGE_ON_NOTICE_VAR_0?"":" while I watch"} can bring that about. To turn it off, run gh pr merge --disable-auto ${SKILL_STEWARD_AUTO_MERGE_ON_NOTICE_VAR_1}.
