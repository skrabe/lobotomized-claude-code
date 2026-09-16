<!--
name: AppifactRepl Input Contains Non-ASCII Space
description: >-
  AppifactRepl input-schema refine error rejecting no-break or ideographic
  spaces that the approval dialog would show as U+0020.
ccVersion: 2.1.273
-->
input contains a space separator other than U+0020 (a no-break or ideographic space, …) that the approval dialog would show as a plain space; write it as a \u escape inside a string
