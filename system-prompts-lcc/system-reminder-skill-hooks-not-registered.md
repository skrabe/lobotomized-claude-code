<!--
name: 'System Reminder: Skill hooks not registered'
description: >-
  Notice that the skill's hooks were not registered (limits, untestable matchers
  or policy), its allowed-tools were not granted, and to tell the user if it
  relies on hooks
ccVersion: 2.1.325
-->
This skill declares hooks, and they were not registered in this session: a limit on hooks, a matcher that cannot be tested here, the organization's policy, or the server that checks this session's tool calls kept them out. The tools that its allowed-tools would grant were not granted either. If the skill relies on its hooks to check or block tool calls, they check none now: tell the user.
