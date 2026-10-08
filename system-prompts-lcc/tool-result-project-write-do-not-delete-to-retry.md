<!--
name: Project write preserve document on retry
description: Warns against deleting an existing document to retry a failed save.
ccVersion: 2.1.294
-->
Do not delete it to retry: this tool cannot undo a delete, and if the retry failed too, the doc would be lost.
