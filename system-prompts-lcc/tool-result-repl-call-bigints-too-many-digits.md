<!--
name: 'REPL: Call BigInts Over Digit Budget'
description: >-
  TypeError thrown into the REPL script when a host call's BigInt arguments
  together exceed the digit budget, telling the model to pass them as text.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_REPL_CALL_BIGINTS_TOO_MANY_DIGITS_VAR_0
-->
REPL: the call was not made, because its BigInts have over ${TOOL_RESULT_REPL_CALL_BIGINTS_TOO_MANY_DIGITS_VAR_0} digits together. Pass them as text.
