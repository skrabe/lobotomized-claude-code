<!--
name: 'Ship: Usage Text'
description: >-
  Usage help for /ship (effort level, PR number/URL, +bot, stop, terms) relayed
  by the skill prompt with 'Tell the user this, in these words'.
ccVersion: 2.1.330
variables:
  - SKILL_SHIP_USAGE_VAR_0
  - SKILL_SHIP_USAGE_VAR_1
-->
Usage: ${SKILL_SHIP_USAGE_VAR_0} [low|medium|high|xhigh|max] [pull request number or URL] [+bot ...]
With no pull request yet, commits and pushes your work and opens one (public repository: commit first). Reviews your change in this session, then watches the pull request for up to ${SKILL_SHIP_USAGE_VAR_1} days.
+name also reads that bot's comments. /ship stop ends the watch. ${SKILL_SHIP_USAGE_VAR_0} terms shows the full terms.
