<!--
name: 'Tool Result: REPL shell immediate reader clause'
description: >-
  Clause explaining that a reader chained right after $ without await reads the
  whole saved output
ccVersion: 2.1.318
-->
A reader called right after $ with no await in between, as in await $`cmd`.text(), reads
