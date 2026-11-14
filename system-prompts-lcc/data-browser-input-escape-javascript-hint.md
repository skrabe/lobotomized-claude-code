<!--
name: 'Data: Browser input escape JavaScript hint'
description: >-
  Hint on writing the escaped character in JavaScript strings or regexes,
  elsewhere literally, and how to keep the escape as text
ccVersion: 2.1.325
variables:
  - DATA_BROWSER_INPUT_ESCAPE_JAVASCRIPT_HINT_VAR_0
-->
${DATA_BROWSER_INPUT_ESCAPE_JAVASCRIPT_HINT_VAR_0.startsWith("\\u00")?`In a JavaScript string or regular expression write \\x${DATA_BROWSER_INPUT_ESCAPE_JAVASCRIPT_HINT_VAR_0.slice(4)}`:`In a JavaScript string write \\u{${DATA_BROWSER_INPUT_ESCAPE_JAVASCRIPT_HINT_VAR_0.slice(2)}}, which a regular expression takes only with the u flag`}; elsewhere write the character itself. To keep the escape as text, write its backslash as \\x5c in JavaScript or, where typing adds to what a field holds, type the backslash and the rest in two actions.
