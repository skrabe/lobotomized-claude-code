<!--
name: 'Tool Hosts Notice: User''s Separate Copy Lives On The Machine'
description: >-
  Shared prefix of the tool-hosts notice for an attached machine that holds the
  user's own separate copy of the project (possibly at another commit, not
  synced either way) plus their apps and processes; its Claude Code may ask
  before running.
ccVersion: 2.1.277
-->
The user's own separate copy of the project is on this machine — it may be at a different commit than this session's checkout, or hold uncommitted work that is not here — along with their other files, applications, local toolchains and running processes. A call run there acts on that copy only, and nothing is synced between it and this session's checkout in either direction; its own Claude Code decides what may run there and may ask the user first.
