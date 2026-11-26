<!--
name: 'Slash Command: Steward repo git config includes a file'
description: Steward refusal when the repository's git config uses include.path
ccVersion: 2.1.332
-->
this repository's own git settings include another file (include.path), which others could rewrite while I watch: copy what you need from that file into your global git config, then run git config --local --unset-all include.path to take the line out
