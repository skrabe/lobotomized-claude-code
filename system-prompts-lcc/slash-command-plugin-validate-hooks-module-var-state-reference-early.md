<!--
name: 'Slash Command: Plugin Validate State Reference Early'
description: Reports a state-reference variable read before its declaration.
ccVersion: 2.1.295
-->
is read here as the file loads, above its declaration, where it is still undefined, so the value it names cannot be listed. Declare it above this read
