<!--
name: 'Tool Description: SearchSkills'
description: >-
  Describes the SearchSkills tool for finding relevant claude.ai skills by
  keyword and suggesting add cards when results fit
ccVersion: 2.1.221
-->

Search the user's claude.ai skills by keyword. Call this when a skill (a reference document or instruction set the user has uploaded or enabled) might help complete the task.

Returns a ranked list with id, name, description, and whether the skill is enabled. When results fit and SuggestSkills is among your tools, call it to render the add card; otherwise relay the relevant results in text instead. If nothing relevant, proceed without mentioning that you searched.
