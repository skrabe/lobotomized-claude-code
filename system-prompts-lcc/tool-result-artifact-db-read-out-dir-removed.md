<!--
name: 'Tool result: Artifact db read out_dir removed'
description: Artifact read_db error when out_dir was removed after a save-to-disk approval.
ccVersion: 2.1.291
-->
this read was approved to save documents under out_dir, and out_dir was removed afterwards — nothing was fetched, so no document entered the conversation; retry so the read is checked as an inline read
