<!--
name: 'Skill: Steward auto-merge turned on during watch'
description: >-
  Warns that auto-merge was turned on after the watch started and how to disable
  it
ccVersion: 2.1.330
variables:
  - SKILL_STEWARD_AUTO_MERGE_TURNED_ON_DURING_WATCH_VAR_0
-->
Auto-merge was turned on for pull request #${SKILL_STEWARD_AUTO_MERGE_TURNED_ON_DURING_WATCH_VAR_0} after the watch started. GitHub merges it once its checks and reviews allow, and what the watch does can bring that about. To turn it off, run gh pr merge --disable-auto ${SKILL_STEWARD_AUTO_MERGE_TURNED_ON_DURING_WATCH_VAR_0}.
