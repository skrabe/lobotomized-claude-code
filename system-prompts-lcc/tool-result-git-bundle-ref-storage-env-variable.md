<!--
name: 'Tool Result: Git bundle GIT_REFERENCE_BACKEND variable'
description: >-
  Working-tree upload refusal reason when the GIT_REFERENCE_BACKEND environment
  variable moves refs elsewhere, telling to start claude without it
ccVersion: 2.1.291
-->
the variable GIT_REFERENCE_BACKEND tells git to keep branches and tags in another place, which this upload does not read; start claude without that variable (a Claude Code settings file may also set it, in its env block)
