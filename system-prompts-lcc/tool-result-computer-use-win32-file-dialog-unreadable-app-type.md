<!--
name: 'Tool result: computer use file dialog target unreadable (app_type)'
description: >-
  Refusal when input could confirm a file dialog whose target can't be read;
  advises app_type overwrite_existing with a full path.
ccVersion: 2.1.332
-->
The input was not sent: it could confirm a file dialog in this app, and where that dialog would save or open cannot be read. Use app_type with overwrite_existing: true on the "File name" box to replace its text with a full path in an ordinary folder, starting with the drive, then confirm again. If you see no such box, or this refusal comes back, ask the user to finish any open file dialog in this app.
