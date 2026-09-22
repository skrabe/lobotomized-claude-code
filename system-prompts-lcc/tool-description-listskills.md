<!--
name: 'Tool Description: ListSkills'
description: >-
  Model-facing prompt/description of the ListSkills tool that lists the user's
  enabled claude.ai skills and points to SuggestSkills.
ccVersion: 2.1.221
-->

List the user's enabled claude.ai skills. Call this when the user asks what skills they have. Pass keywords to filter to a topic; omit to list all. To recommend skills they do NOT have yet, use SuggestSkills when it is among your tools; otherwise use SearchSkills and relay the relevant results in text instead.
