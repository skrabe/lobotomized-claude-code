<!--
name: 'Tool result: REPL context reset after globalThis change'
description: >-
  Error returned when an earlier REPL script changed globalThis so new calls
  cannot start; the context was reset and the call must be rerun.
ccVersion: 2.1.318
-->
This REPL call did not run: an earlier script changed globalThis (for example, its prototype) in a way that stops new calls from starting. The REPL context was reset, so variables and functions from earlier calls are gone. Rerun this call's code, and don't change globalThis itself again.
