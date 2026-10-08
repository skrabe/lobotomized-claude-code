<!--
name: Artifact database file lacks identity
description: Refuses a database JSON upload when the file cannot be identified safely.
ccVersion: 2.1.294
-->
file_path is on a volume that reports no usable file identity (some network, FUSE, and virtual-disk mounts), so the approved file cannot be told apart from a replacement — copy it to an ordinary local directory and pass the copy
