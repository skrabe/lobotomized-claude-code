<!--
name: 'System Reminder: Unreachable attached machines (rechecked)'
description: >-
  Says the session rechecks unreachable machines a few times in the next five
  minutes and notes any that answer, then explains that a later call takes up to
  10 seconds to fail and should wait for the user
ccVersion: 2.1.295
variables:
  - UNREACHABLE_MACHINES_NOTICE
  - OFFLINE_MACHINE_PRONOUN
  - IS_SINGLE_OFFLINE_MACHINE
  - CALL_BASED_RETRY_GUIDANCE
-->
${UNREACHABLE_MACHINES_NOTICE} This session checks ${OFFLINE_MACHINE_PRONOUN} again a few times in the next five minutes, and a later copy of this note says so if ${IS_SINGLE_OFFLINE_MACHINE?"it":"one"} answers. After that a call to ${IS_SINGLE_OFFLINE_MACHINE?"it":"one of them"}, which takes up to 10 seconds to fail, ${CALL_BASED_RETRY_GUIDANCE}
