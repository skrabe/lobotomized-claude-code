<!--
name: 'Tool Result: Bash dangerous operation — derived value, cd of empty input'
description: >-
  Clause describing what a variable assigned from a `cd ... && pwd` substitution
  becomes when its input is empty: the current directory. It is spliced into the
  derived-variable dangerous-removal message.
ccVersion: 2.1.281
-->
prints the current directory when its input is empty (`cd ""` stays put)
