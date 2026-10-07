<!--
name: 'Tool Result: Project write over max size'
description: >-
  Project write refusal when the write would exceed the project's maximum
  knowledge size; warns not to delete docs to retry and to tell the user the
  project is out of room
ccVersion: 2.1.292
-->
Write refused; nothing in the project was changed. This write would put the project over its maximum size. Any doc already at this path still holds its old content; do not delete it to retry, because the retry can be refused too, and the content would then be lost. Do not delete other docs to make room unless the user asks. Tell the user the project is out of room: they can remove docs or files they no longer need, or ask you to write less.
