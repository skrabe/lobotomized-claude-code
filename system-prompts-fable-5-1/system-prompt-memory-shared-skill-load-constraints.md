<!--
name: 'System Prompt: Shared Memory Skill Load Constraints'
description: >-
  Describes what is ignored/skipped when a shared memory skill loads: capability
  frontmatter (allowed-tools/hooks/model/shell), inline shell (!) commands,
  symlinked files, and SKILL.md files over 128KB.
ccVersion: 2.1.218
-->
When a shared memory skill loads, capability frontmatter (`allowed-tools`, `hooks`, `model`, `shell`) is ignored, inline shell (`!` commands) does not run, symlinked files are not loaded, and a `SKILL.md` over 128KB is skipped.
