<!--
name: 'Skill: Claude Test Description Spec Runner'
description: >-
  Body of the Claude Test skill description: specs run in a fenced headless
  browser and return a PASS/FAIL summary.
ccVersion: 2.1.274
-->
plain-language specs in .claude-test/specs/ run in the background in a fenced headless browser against the local dev server, and a PASS / FAIL summary comes back with screenshots. On a first run it proposes a starter set of specs for the person to approve. Use when the user asks ("test my app", "did I break anything?", "run claude test").
