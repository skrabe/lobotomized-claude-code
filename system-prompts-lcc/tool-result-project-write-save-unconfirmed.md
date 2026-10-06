<!--
name: 'Tool Result: project_write save unconfirmed'
description: >-
  project_write error when the new content could not be confirmed as saved;
  instructs the model to project_read before retrying.
ccVersion: 2.1.291
-->
project_write: could not confirm that the new content was saved. Nothing was removed, so the project may now list this path twice. Call project_read on this path before any other write or delete: if it returns the new content, stop and tell the user that an earlier copy may need removing from the project in claude.ai; if not, you may try the write once more.
