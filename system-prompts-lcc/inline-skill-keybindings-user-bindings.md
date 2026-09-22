<!--
name: 'Inline blob: skill keybindings user bindings'
description: 'keybindings-help skill: how user bindings interact with defaults.'
inlineBlobAnchor: '[$\w]+=\["## How User Bindings Interact with Defaults",'
inlineBlobKind: 'array'
injectionGate: 'keybindings-help skill'
ccVersion: '2.1.138'
-->

## How User Bindings Interact with Defaults

- User bindings are **additive** — they are appended after the default bindings
- To **move** a binding to a different key: unbind the old key (`null`) AND add the new binding
- A context only needs to appear in the user's file if they want to change something in that context
