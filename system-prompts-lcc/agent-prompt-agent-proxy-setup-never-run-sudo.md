<!--
name: 'Agent prompt: agent proxy setup never run sudo'
description: >-
  Instructs the session never to run sudo and to have the user run root steps in
  another terminal, then check results
ccVersion: 2.1.332
-->
Never run sudo yourself. This session denies it to Bash as a guard, not a boundary. For each step that needs root, show the user the exact command and why, have them run it in another terminal (a sudo in this one could leave a cached credential this session could use), then check its result before going on.
