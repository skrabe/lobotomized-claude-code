<!--
name: 'System Reminder: GitHub API rate limit exceeded'
description: >-
  Reminder warning the model that the shared GitHub API rate limit is exhausted
  and to sleep until reset.
ccVersion: 2.1.178
-->
<system-reminder>GitHub API rate limit exceeded (5,000/hr shared across all tools and agents). Run `gh api rate_limit --jq .resources` and wait until reset before more gh calls. If polling, use ScheduleWakeup instead of retrying.</system-reminder>
