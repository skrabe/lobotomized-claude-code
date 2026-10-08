<!--
name: Artifact Database Write Source Changed
description: Refuses a database write when its approved local file changed.
ccVersion: 2.1.294
-->
file_path no longer names the file that was approved (it moved, was replaced, or was rewritten) — retry the write so it is checked again
