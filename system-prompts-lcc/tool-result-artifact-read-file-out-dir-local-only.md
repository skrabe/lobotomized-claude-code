<!--
name: Artifact File Read Output Must Be Local
description: Rejects artifact file downloads whose destination is a network path.
ccVersion: 2.1.294
-->
read_file saves only to local directories — out_dir names a network path or cannot be resolved
