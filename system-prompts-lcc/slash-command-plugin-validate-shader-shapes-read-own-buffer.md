<!--
name: 'Shader refusal: shapes read empty target'
description: Shader refusal when shapes read the empty buffer they draw into.
ccVersion: 2.1.326
-->
shapes cannot read the empty buffer they draw into: it would give zeros, so give that buffer a body or read another
