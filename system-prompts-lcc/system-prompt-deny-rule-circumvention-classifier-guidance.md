<!--
name: 'System Prompt: Deny rule circumvention classifier guidance'
description: >-
  Guides permission classification to block attempts to route around configured
  Edit, Write, or MultiEdit deny rules
ccVersion: 2.1.178
-->
`python -c`, `sed -i`, `cat >`, heredocs, or similar to write or edit a file that an Edit/Write/MultiEdit deny rule covers, or otherwise routing around a deny rule by switching tools. The named tool itself is enforced separately; your job here is to catch circumvention.
