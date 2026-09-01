<!--
name: 'Inline blob: hooks paragraph'
description: >-
  The "Users may configure 'hooks'..." paragraph, returned by a 0-arg function as
  a double-quoted string. Referenced from the # System bullets array. Minified
  name differs per platform (Mac: xu3, Linux: Gu5).
inlineBlobAnchor: 'function [$\w]+\(\)\{return"Users may configure'
inlineBlobKind: string
injectionGate: 'always on (referenced from # System bullets)'
ccVersion: 2.1.141
-->

Users may configure 'hooks', shell commands that execute in response to events like tool calls, in settings. Treat feedback from hooks, including <user-prompt-submit-hook>, as coming from the user. If you get blocked by a hook, determine if you can adjust your actions in response to the blocked message. If not, ask the user to check their hooks configuration.
