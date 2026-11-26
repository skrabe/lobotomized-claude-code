<!--
name: 'Tool result: computer use file dialog runnable type (app_type)'
description: >-
  Refusal when the File name box ends in a runnable file type; advises app_type
  with overwrite_existing to rename.
ccVersion: 2.1.332
-->
The input was not sent: the name in the "File name" box ends in a file type that Windows can run when it is opened, such as .bat, .js or .url. Another folder or a full path will not help. If the user needs this file type, ask them to save or open the file themselves. To save under another type instead, press Escape if a prompt is up, use app_type with overwrite_existing: true on the box to enter a name such as notes.txt, and tell the user what you changed.
