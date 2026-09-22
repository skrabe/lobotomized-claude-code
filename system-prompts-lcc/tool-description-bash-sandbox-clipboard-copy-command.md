<!--
name: 'Tool Description: Bash Sandbox Clipboard Copy Command'
description: >-
  Sandbox bash-tool description: if pbcopy/xclip/wl-copy fail, emit a fenced
  block and tell the user to run /copy.
ccVersion: 2.1.267
-->
If a clipboard utility such as `pbcopy`, `xclip`, or `wl-copy` fails inside the sandbox and the user wants the text on their clipboard, put the text in a fenced code block in your response and tell them to run `/copy` (it copies from outside the sandbox; when the picker appears they can select just that block), rather than writing a file for them to copy manually.
