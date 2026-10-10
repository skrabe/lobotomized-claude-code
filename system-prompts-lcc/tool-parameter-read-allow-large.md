<!--
name: 'Tool Parameter: Read allow large'
description: >-
  Read tool parameter describing reading a file over the usual size limits up to
  what fits in context
ccVersion: 2.1.296
-->
Set to true to read a text file, or a line range of one, that is over the usual size limits, up to what still fits in your context. Only use this when you genuinely need all of it or the user asked for the whole file; otherwise read it in parts with offset and limit, or search it.
