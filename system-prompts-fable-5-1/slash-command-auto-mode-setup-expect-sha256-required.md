<!--
name: 'Slash Command: /auto-mode-setup --expect-sha256 required'
description: >-
  Non-interactive apply error: --expect-sha256 (64-hex proposal digest) must be
  passed before --apply-file.
ccVersion: 2.1.218
-->
--expect-sha256 is required: pass the 64-character hex sha256 of the proposal file’s exact bytes, before --apply-file. Every non-interactive apply is hash-bound.
