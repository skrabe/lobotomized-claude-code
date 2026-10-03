<!--
name: 'Skill: Claude Test when to use'
description: >-
  whenToUse text for the claude-test skill: what it checks, how specs run, when
  to offer or run it
ccVersion: 2.1.288
-->
specs in .claude-test/specs/ run in the background in a fenced headless browser against the local dev server, and a PASS / FAIL summary comes back with screenshots. On a first run it proposes a starter set of specs for the person to approve. Use when the user asks ("test my app", "did I break anything?", "run claude test"). When the user asks for it. Unasked, only in a project that already has .claude-test/specs/ and only after a change a person can see in 
