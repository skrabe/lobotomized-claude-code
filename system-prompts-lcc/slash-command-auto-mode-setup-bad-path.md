<!--
name: auto-mode-setup bad-path reason
description: >-
  bad_path error reason returned by /auto-mode-setup --apply-file when the
  proposal path isn't under an allowed dir; model-visible command result.
ccVersion: 2.1.210
-->
Pass an absolute path under the system temp directory or the Claude config directory — --apply-file only reads proposal files the reviewing host wrote there.
