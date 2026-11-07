<!--
name: 'Tool Result: Artifact DB shared version no database, user cannot add'
description: >-
  Prefix to an artifact database error when the shared version has no database
  and only a publisher, not the user, can add one.
ccVersion: 2.1.319
-->
Do not retry: the version of this artifact shared with the user has no database, so every database call on it is refused; only someone who can publish it can add one, and the user cannot.
