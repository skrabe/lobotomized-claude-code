<!--
name: 'Tool Parameter: Artifact Page Flag'
description: >-
  Schema description for the Artifact tool's optional page flag, including that
  a type-created Artifact omits its page on read when type instructions come
  with it.
ccVersion: 2.1.325
-->
read only: pass page: true for the rendered page itself where a read otherwise answers something else — a read of an Artifact created from an Artifact type leaves its page out when the type's instructions come with it (the page is the type's own, the same on every Artifact made from it).
