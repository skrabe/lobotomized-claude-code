<!--
name: 'Tool Result: Workshop decisions island grammar'
description: >-
  Verifier violation when the ws-decisions island does not match the required
  entry grammar and resolution invariant
ccVersion: 2.1.219
-->
The ws-decisions island failed the entry grammar: one {"items":[…]} object, each entry exactly {id, opts, state, choice, custom} with slug ids and opts, state open|resolved, and the resolution invariant (open: neither choice nor custom; resolved: exactly one). Re-emit the island from your decision blocks.
