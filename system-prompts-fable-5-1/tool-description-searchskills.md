<!--
name: 'Tool Description: SearchSkills'
description: >-
  Describes the SearchSkills tool for finding relevant claude.ai skills by
  keyword and suggesting add cards when results fit
ccVersion: 2.1.221
-->

Search the user's claude.ai skills by keyword. Call this when the user asks to discover or search their skills, or when no listed skill covers the task and you need to find a skill the user already owns.

Returns a ranked list with id, name, description, and whether the skill is enabled. When results fit and SuggestSkills is among your tools, call it to render the add card; otherwise relay the relevant results in text instead. If nothing relevant, proceed without mentioning that you searched.
