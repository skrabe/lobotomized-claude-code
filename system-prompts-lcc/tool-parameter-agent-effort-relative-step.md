<!--
name: 'Tool Parameter: Agent effort (relative step)'
description: >-
  Agent tool effort parameter description (variant with lower/higher steps)
  explaining when to pass lower or higher relative to the default effort,
  opening the list of named levels.
ccVersion: 2.1.296
-->
Reasoning effort for this agent. "lower" or "higher" is one step from the effort the agent would otherwise run at (normally yours), on whatever model it would otherwise use. Pass "lower" when the brief is mechanical and checkable against itself — bounded search, grep-and-report, a pattern you spelled out. Pass "higher" when one well-specified piece needs more reasoning than the work around it. Omit when neither clearly applies. Name a level (
