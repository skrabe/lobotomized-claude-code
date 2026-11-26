<!--
name: 'Tool result: computer use file dialog name off-limits (app_type)'
description: >-
  Refusal when the File name box points off-limits or holds an uncheckable form;
  advises app_type overwrite_existing.
ccVersion: 2.1.332
-->
The input was not sent: the "File name" box points to a file or folder that is off-limits, or holds a form that cannot be checked: a short name such as ABC~1, a location such as shell:documents, a %VARIABLE% beside ".." or joined to a name, or very long text. If a prompt is up, press Escape first. Then use app_type with overwrite_existing: true on the box to replace its text with a full path in an ordinary folder, starting with the drive.
