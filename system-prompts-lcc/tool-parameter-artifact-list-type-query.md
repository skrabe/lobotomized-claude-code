<!--
name: 'Tool Parameter: Artifact List type_query'
description: >-
  Artifact tool type_query parameter (list with scope 'types'): narrows the
  types listing by relevance, warns that a narrowed listing is not the whole
  catalog, and says to omit it when choosing a type.
ccVersion: 2.1.277
-->
list with scope 'types' only: limits the listing to the types whose title or description match this text best, ignoring case; a type that matches less well is left out, so a narrowed listing is not the whole catalog. Claude omits it when choosing a type for a request, unless a listing made without it says more types exist than it shows.
