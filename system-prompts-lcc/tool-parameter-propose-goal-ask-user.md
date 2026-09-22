<!--
name: 'Tool Parameter: Propose Goal Ask User'
description: >-
  Describes when the model may bypass user approval through the ProposeGoal
  tool's ask_user input.
ccVersion: 2.1.227
-->
Whether to ask the user for approval before the goal is set. Defaults to true — an approval dialog is shown. Set false ONLY when the user's own words in this conversation stated this outcome as what they want; the goal is then set directly, with a visible notice in the transcript, and the user can clear it with /goal clear.
