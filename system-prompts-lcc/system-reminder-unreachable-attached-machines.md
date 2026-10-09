<!--
name: 'System Reminder: Unreachable attached machines'
description: >-
  Lists attached machines that are not reachable and directs doing all other
  work here this turn, reporting what is waiting, not substituting for or
  handing work to other machines, and making a single retry call only when the
  user asks, never waiting or polling
ccVersion: 2.1.295
variables:
  - FORMAT_MACHINE_NAME_LIST_FN
  - OFFLINE_MACHINE_NAMES
  - OFFLINE_MACHINE_PRONOUN
  - IS_SINGLE_OFFLINE_MACHINE
  - HAS_OTHER_ONLINE_MACHINES
-->
- Not reachable right now: ${FORMAT_MACHINE_NAME_LIST_FN(OFFLINE_MACHINE_NAMES)}. Do not call ${OFFLINE_MACHINE_PRONOUN}. Do everything in the task that does not need ${OFFLINE_MACHINE_PRONOUN}, here, in this turn; then, if anything is waiting on ${OFFLINE_MACHINE_PRONOUN}, tell the user ${IS_SINGLE_OFFLINE_MACHINE?"their machine is":"which machines are"} not answering (asleep, offline, or Claude Code not running there) and exactly what is waiting. Do not stand in for ${OFFLINE_MACHINE_PRONOUN} here, and do not stop at "tell me when ${IS_SINGLE_OFFLINE_MACHINE?"it is":"they are"} back" while other work remains.${HAS_OTHER_ONLINE_MACHINES?` Do not hand ${IS_SINGLE_OFFLINE_MACHINE?"its":"their"} work to another machine unless the task belongs there: what is only on ${OFFLINE_MACHINE_PRONOUN} is not on the others.`:""}
