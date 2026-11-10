<!--
name: 'Tool result: project_write cannot check for changes'
description: >-
  project_write refusal when the session cannot check whether the doc changed;
  forbids delete-to-rewrite and tells the model to inform the user.
ccVersion: 2.1.322
-->
Write refused; nothing in the project was changed. This session cannot check whether this doc has changed since you last read or wrote it, so it does not replace it. Do not delete the doc to write it afresh. Tell the user that the content was not saved, and offer it to them another way.
