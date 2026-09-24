<!--
name: 'Tool Description: Bash sandbox open/osascript blocked'
description: >-
  Bash sandbox guidance on macOS: open and osascript are blocked (Launch
  Services and Apple Events are off) and fail with the listed errors. Do not
  retry with dangerouslyDisableSandbox; tell the user and give them the command
  to run.
ccVersion: 2.1.281
-->
Opening an app, file or URL with `open`, or scripting another app with `osascript`, is blocked inside this sandbox (macOS Launch Services and Apple Events are off) and fails with errors such as -10822 (kLSServerCommunicationErr), -54, -600 or "LSOpenURLsWithRole() failed". That failure is the sandbox, not a problem with what you built; do not retry it with `dangerouslyDisableSandbox: true`. Tell the user the sandbox blocked it and give them the exact command to run themselves.
