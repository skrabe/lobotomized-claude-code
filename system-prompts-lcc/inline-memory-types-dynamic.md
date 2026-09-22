<!--
name: 'Inline blob: memory types dynamic'
description: >-
  The lean "## Types of memory" block (dynamic list over the type names +
  memory-types skill pointer) rendered when the tengu_ochre_finch gate is on
  (forced by tweakcc-fixed's lean-memory-types toggle). Raw passthrough —
  free identifiers (H, Fu5, lL8) are remapped positionally; keep them in
  this order when editing.
inlineBlobAnchor: 'return\["## Types of memory","","Save a memory when you learn one of the following'
inlineBlobKind: 'array'
inlineBlobRawPassthrough: 'true'
injectionGate: 'memory prompts when the lean-memory-types gate is on'
ccVersion: '2.1.179'
-->
"## Types of memory","","Save a memory when you learn one of the following — pick the matching `type:`:","",...H.map((_)=>`- **${_}** — ${Fu5[_]}`),"",`Invoke the \`${lL8}\` skill for scope, body structure and examples once you've decided to save.`,""
