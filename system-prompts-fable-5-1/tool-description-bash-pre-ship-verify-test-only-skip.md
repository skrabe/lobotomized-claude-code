<!--
name: Bash Pre-Ship Verify Test-Only Skip
description: >-
  Explains in the Bash tool prompt that /verify may be skipped only for
  test-only or otherwise runtime-surface-free diffs.
ccVersion: 2.1.226
variables:
  - TOOL_DESCRIPTION_BASH_PRE_SHIP_VERIFY_TEST_ONLY_SKIP_VAR_0
-->
 Also skip \`/${TOOL_DESCRIPTION_BASH_PRE_SHIP_VERIFY_TEST_ONLY_SKIP_VAR_0}\` — and only it — when the diff touches only tests or other code with no runtime surface to drive end-to-end (a change to product source always has one), and say in that sentence that you skipped it for that reason, naming the files that make the diff test-only or surface-free.
