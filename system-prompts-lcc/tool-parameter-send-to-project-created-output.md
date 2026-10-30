<!--
name: 'Tool parameter: Send to project created result field'
description: >-
  outputSchema describe() on the Send to project tool's created field,
  explaining what created true/false means and pointing to reason and mayExist.
ccVersion: 2.1.314
-->
Whether the call went through: a project was created (mode 'new') or the existing project was reached (mode 'existing'; savedToMemory and handedOff say what landed there). False means nothing was created or sent; see reason and mayExist.
