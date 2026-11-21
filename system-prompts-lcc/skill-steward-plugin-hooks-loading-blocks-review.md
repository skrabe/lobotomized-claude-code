<!--
name: 'Skill: Steward plugin hooks loading blocks review'
description: Reason a review cannot run under a watch while plugin hooks are still loading
ccVersion: 2.1.330
variables:
  - SKILL_STEWARD_PLUGIN_HOOKS_LOADING_BLOCKS_REVIEW_VAR_0
-->
a plugin's hooks are still loading, so I can't tell yet whether a ConfigChange hook is set, and a review under a watch would reload your skills without asking one. After this review, run /${SKILL_STEWARD_PLUGIN_HOOKS_LOADING_BLOCKS_REVIEW_VAR_0} to watch
