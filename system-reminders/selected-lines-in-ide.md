<!--
name: IDE selected-lines reminder
description: >-
  Fires when an IDE selection is sent into chat. Conditional. Empty .md body =
  silent selection (model not told what user selected).
ccVersion: 2.1.141
placeholders:
  - line_start
  - line_end
  - filename
  - selected_text
shadows:
  - system-reminder-lines-selected-in-ide
-->

The user selected the lines {{line_start}} to {{line_end}} from {{filename}}:
{{selected_text}}

This may or may not be related to the current task.
