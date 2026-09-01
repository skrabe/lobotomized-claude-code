<!--
name: 'Inline blob: loop tick autonomous'
description: '/loop tick prompt for autonomous mode (no user prompt).'
inlineBlobAnchor: "`# Autonomous loop tick \\(dynamic pacing\\)"
inlineBlobKind: 'template'
injectionGate: '/loop autonomous run, no user prompt'
ccVersion: '2.1.138'
-->
# Autonomous loop tick (dynamic pacing)

Run the autonomous check using the loop instructions established earlier in this conversation. If you cannot find them, treat this as a no-op tick.

You scheduled this tick via the ${dY} tool (not a recurring cron). To keep the loop alive, call ${dY} again at the end of this turn with `prompt` set to the literal sentinel `${GJH}` — otherwise the loop ends after this tick.${bV8}${aX_()}
