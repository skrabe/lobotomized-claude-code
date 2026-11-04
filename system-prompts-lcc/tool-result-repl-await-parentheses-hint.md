<!--
name: 'Tool result: REPL await parentheses hint'
description: >-
  Hint appended to a REPL script error when a promise from
  file().text()/json()/lines() was chained without awaiting
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_AWAIT_PARENTHESES_HINT_VAR_0
  - TOOL_RESULT_REPL_AWAIT_PARENTHESES_HINT_VAR_1
-->
Hint: \`.${TOOL_RESULT_REPL_AWAIT_PARENTHESES_HINT_VAR_0}()\` returns a promise: \`(await file(p).${TOOL_RESULT_REPL_AWAIT_PARENTHESES_HINT_VAR_0}()).${TOOL_RESULT_REPL_AWAIT_PARENTHESES_HINT_VAR_1}(…)\` — the await needs its own parentheses before the next method.
