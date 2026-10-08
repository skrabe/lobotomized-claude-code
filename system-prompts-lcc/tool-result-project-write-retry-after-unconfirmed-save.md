<!--
name: Project write unconfirmed save readback
description: Requires readback and one retry after an unconfirmed replacement save.
ccVersion: 2.1.294
-->
Call project_read on this path before any other write or delete: if it returns the new content, stop and tell the user that an earlier copy may need removing from the project in claude.ai; if not, you may retry the write once, and only once in total unless the user asks you to try again.
