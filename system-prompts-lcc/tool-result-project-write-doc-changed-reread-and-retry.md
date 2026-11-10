<!--
name: 'Tool result: project_write doc changed'
description: >-
  project_write refusal when the doc changed since last read; tells the model to
  project_read, edit the returned text and write again.
ccVersion: 2.1.322
-->
Write refused; nothing in the project was changed. The doc at this path has changed since you last read or wrote it in this conversation. Call project_read on this path, make your change in the text that it returns, and write again. If project_read cannot show the whole text inline, follow what its result tells you instead; if the write is refused again, tell the user that the new content was not saved, and offer it to them another way. Do not delete the doc to write it afresh.
