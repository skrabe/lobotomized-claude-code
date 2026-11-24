<!--
name: 'Ship Steward: Usage Text'
description: >-
  Usage help for the watch-only /ship:steward command (PR number/URL, +bot,
  stop, terms; points to the reviewing command) relayed via the skill prompt.
ccVersion: 2.1.331
variables:
  - SKILL_SHIP_STEWARD_USAGE_VAR_0
  - SKILL_SHIP_STEWARD_USAGE_VAR_1
  - SKILL_SHIP_STEWARD_USAGE_VAR_2
-->
Usage: /${SKILL_SHIP_STEWARD_USAGE_VAR_0} [pull request number or URL] [+bot ...] | stop | terms
Watches your open GitHub pull request, checked out here, for up to ${SKILL_SHIP_STEWARD_USAGE_VAR_1} days: failed checks, conflicts, review comments.
+bot also reads that bot's comments. To review the code first, use ${SKILL_SHIP_STEWARD_USAGE_VAR_2}.
