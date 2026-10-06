<!--
name: 'Tool Result: workflow parallel() expects functions'
description: >-
  TypeError thrown into a workflow script when parallel() receives promises
  instead of functions, telling it to wrap each call as () => agent(...).
ccVersion: 2.1.291
-->
parallel() expects an array of functions, not promises. Wrap each call: () => agent(...)
