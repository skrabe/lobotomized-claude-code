<!--
name: Project delete cannot undo
description: >-
  Reminds the model that project deletion is irreversible and project_write
  replaces documents in place.
ccVersion: 2.1.294
-->
This tool cannot undo a delete. To change a doc, do not delete it first: project_write to its path replaces the content in place.
