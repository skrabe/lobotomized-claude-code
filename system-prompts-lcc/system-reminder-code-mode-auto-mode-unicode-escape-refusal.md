<!--
name: 'System Reminder: Code Mode auto mode unicode escape refusal'
description: >-
  Refuses Code Mode code containing a \uXXXX escape that auto mode cannot check
  and asks for the characters to be written another way
ccVersion: 2.1.318
-->
This code was NOT run. Auto mode could not check it, because it contains a \uXXXX escape. This is not a judgment that the code is unsafe. Write each such character another way, for example \x1b or \u{1b} in place of \u001b, and send the code again.
