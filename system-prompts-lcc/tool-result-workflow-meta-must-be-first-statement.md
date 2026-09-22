<!--
name: 'Tool Result: Workflow script — meta must be the first statement'
description: >-
  The Workflow tool parse error stating that the `export const meta` block must
  be the first statement in the script. Returned by validateInput and thrown
  from call(), so it reaches the model whether or not a slash command is
  involved.
ccVersion: 2.1.233
-->
`export const meta = { name, description, phases }` must be the FIRST statement in the script
