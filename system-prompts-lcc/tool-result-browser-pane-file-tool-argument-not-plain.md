<!--
name: 'Tool Result: Browser pane file tool argument not plain'
description: >-
  Tells Claude nothing was saved because a value has an = sign or is too long,
  how to fix the path or origin, and when to stop and tell the user
ccVersion: 2.1.328
-->
Nothing was saved or uploaded. A value has "=" or a sign like it, or the values are too long. If it is a path, copy the file to a short path without that sign. If it is origin, send the site alone, with no path or query. Then call the tool again. If neither helps, tell the user, and do not retry.
