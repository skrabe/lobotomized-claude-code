<!--
name: 'Tool Result: Project write refused, doc over size limit'
description: >-
  Projects write error saying the text exceeds the 1.9 MB per-doc limit, the old
  doc is kept, not to delete it to retry, and to offer splitting.
ccVersion: 2.1.325
-->
Write refused; nothing in the project was changed. This text is over the 1.9 MB limit for one doc. Any doc already at this path still holds its old content; do not delete it to retry, because the retry can be refused too, and the old content would then be lost. Tell the user the text was not saved, and offer to split it into smaller docs or shorten it.
