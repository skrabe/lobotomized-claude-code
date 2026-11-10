<!--
name: 'Tool result: project_write doc changed (file variant)'
description: >-
  project_write refusal when the doc changed since last read; tells the model to
  project_read, re-save the file and repeat the write, or tell the user.
ccVersion: 2.1.322
-->
Write refused; nothing in the project was changed. The doc at this path has changed since you last read or wrote it in this conversation. Call project_read on this path, make your change from the text that it shows or saves whole, write the file again, and repeat this project_write. If it says that only part of the doc was saved or shown, or the write is refused again, tell the user that the new content was not saved, and offer it to them another way. Do not delete the doc to write it afresh.
