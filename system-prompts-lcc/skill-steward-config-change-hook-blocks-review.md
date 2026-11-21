<!--
name: 'Skill: Steward ConfigChange hook blocks review'
description: Reason a review cannot run under a watch when a ConfigChange hook is set
ccVersion: 2.1.330
variables:
  - SKILL_STEWARD_CONFIG_CHANGE_HOOK_BLOCKS_REVIEW_VAR_0
-->
a ConfigChange hook is set (for example in your settings, your organization's managed settings, or a plugin), and a review under a watch would reload your skills without asking that hook. To watch without a review, run /${SKILL_STEWARD_CONFIG_CHANGE_HOOK_BLOCKS_REVIEW_VAR_0}
