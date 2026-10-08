<!--
name: Artifact Database Read Output Must Be Local
description: Rejects database read output paths that resolve to a network location.
ccVersion: 2.1.294
-->
read_db saves only to local directories — out_dir names a network path or cannot be resolved
