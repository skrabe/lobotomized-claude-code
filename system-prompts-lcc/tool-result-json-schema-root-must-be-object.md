<!--
name: JSON Schema Root Must Be Object
description: >-
  Finding message requiring type: object at the schema root; interpolated as
  ${ie} in the workflow agent() throw.
ccVersion: 2.1.261
-->
the root schema must declare type: 'object' (the API rejects any other root type for a tool input schema); wrap arrays or primitives in an object property
