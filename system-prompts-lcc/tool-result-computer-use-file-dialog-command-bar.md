<!--
name: 'Computer use: file dialog command bar'
description: >-
  Refusal when a click would land on a Windows file dialog command bar or field
  label.
ccVersion: 2.1.330
-->
A click at these coordinates would land on the file dialog's command bar (Organize, New folder, the view buttons), or on a field label or the blank space around one, which this check cannot tell from the bar. The whole bar is blocked because its Organize menu can delete, move and rename files and open their Properties. To use a field, click inside its box, not on its label. The file list, the navigation pane and the Back / Up arrows still work here.
