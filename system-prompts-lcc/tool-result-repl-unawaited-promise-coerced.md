<!--
name: 'Tool Result: REPL unawaited promise coerced'
description: >-
  Error when an unawaited Promise is coerced to string, explaining where await
  is needed
ccVersion: 2.1.318
-->
REPL: unawaited Promise coerced to string. A result used inline needs 'await' — e.g. const c = await file(f).text(); await write(f, c + s). Only the top-level keys of a returned object are awaited for you.
