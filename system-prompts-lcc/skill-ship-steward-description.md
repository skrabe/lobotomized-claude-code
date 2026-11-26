<!--
name: 'Ship Steward: Skill Description'
description: >-
  Bundled /ship:steward (watch-only) skill description: watch the current
  branch's open PR and handle CI failures, conflicts and review comments until
  merged or closed, without reviewing first; never merges.
ccVersion: 2.1.332
variables:
  - SKILL_SHIP_STEWARD_DESCRIPTION_VAR_0
-->
Watch the current branch's open pull request in this session and handle CI failures, conflicts, and review comments until it's merged or closed, for up to ${SKILL_SHIP_STEWARD_DESCRIPTION_VAR_0} days. It doesn't review the code first. Claude is told never to merge the pull request.
