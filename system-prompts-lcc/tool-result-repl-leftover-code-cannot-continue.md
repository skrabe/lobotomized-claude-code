<!--
name: 'Tool Result: REPL leftover code cannot continue'
description: >-
  Late report telling that code a script left running cannot use timers or make
  new calls, and to await the rest inside one script
ccVersion: 2.1.330
-->
Code that this script left running can go no further: after a script returns, that code can't use sleep() or timers, and it can make calls only while an earlier call is still running. Check what was done, then await the rest inside one script (set the timeout parameter for a long loop).
