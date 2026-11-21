<!--
name: 'Ship: Watch Deny Rule Forbids Command'
description: >-
  Reason in the /ship watch-start report naming the deny rule source and the
  gh/git command it forbids that the PR watch needs.
ccVersion: 2.1.330
variables:
  - SKILL_SHIP_WATCH_DENY_RULE_FORBIDS_COMMAND_VAR_0
  - SKILL_SHIP_WATCH_DENY_RULE_FORBIDS_COMMAND_VAR_1
-->
a deny rule from ${SKILL_SHIP_WATCH_DENY_RULE_FORBIDS_COMMAND_VAR_0(SKILL_SHIP_WATCH_DENY_RULE_FORBIDS_COMMAND_VAR_1.rule.source)} forbids ${SKILL_SHIP_WATCH_DENY_RULE_FORBIDS_COMMAND_VAR_1.does}, ${SKILL_SHIP_WATCH_DENY_RULE_FORBIDS_COMMAND_VAR_1.does==="gh pr comment"?"and a watch comments on the pull request":"which a watch runs"} (see /permissions)
