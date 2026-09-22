<!--
name: 'Skill: /code-review efficiency dimension'
description: >-
  Code-review dimension: flag wasted work the diff introduces (redundant
  computation/IO, needless sequential work, closures that retain large scopes)
  and name the cheaper alternative
ccVersion: 2.1.169
-->
### Efficiency

Flag wasted work the diff introduces: redundant computation or repeated I/O,
independent operations run sequentially, blocking work added to startup or
hot paths. Also flag long-lived objects built from closures or captured
environments — they keep the entire enclosing scope alive for the object's
lifetime (a memory leak when that scope holds large values); prefer a
class/struct that copies only the fields it needs. Name the cheaper
alternative.
