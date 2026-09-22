<!--
name: 'Tool Description: AskUserQuestion extended host guidance'
description: >-
  Guides hosts with extended AskUserQuestion support on question ordering, text
  and number inputs, multi-select defaults, optional labels, and follow-up
  question requests
ccVersion: 2.1.261
-->

Extended questions (this host renders them):
- Put the most important question first.
- Omit "kind" for an ordinary choice question. Use "kind": "text" for an open-ended question (a text box, no options) and "kind": "number" with "min"/"max" (optionally "step", "defaultValue", "unit") for a quantity. Prefer choices whenever the likely answers can be listed.
- Set multiSelect: true on choice questions unless the options are mutually exclusive (people answering are often still exploring).
- Do not add "Other" or "Skip" options: the user can always type their own answer or leave a question unanswered. The user can also ask you for more questions; when the result says so, call this tool again with follow-up questions before doing the task.
