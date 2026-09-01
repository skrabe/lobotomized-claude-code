<!--
name: 'Inline blob: loop tick tasks'
description: '/loop tick prompt when loop.md has tasks (dynamic-pacing mode).'
inlineBlobAnchor: "`# /loop tick \\\\u2014 loop\\.md tasks \\(dynamic pacing\\)"
inlineBlobKind: 'template'
injectionGate: '/loop autonomous run, loop.md present'
ccVersion: '2.1.138'
-->
# /loop tick — loop.md tasks (dynamic pacing)

Work the tasks from the loop.md contents established earlier in this conversation. If you cannot find them, treat this as a no-op tick.

You scheduled this tick via the ${dY} tool (not a recurring cron). To keep the loop alive, call ${dY} again at the end of this turn with `prompt` set to the literal sentinel `${sX_}` — otherwise the loop ends after this tick.${bV8}${aX_(!0)}
