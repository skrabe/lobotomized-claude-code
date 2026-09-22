<!--
name: 'Tool Parameter: Artifact list_types type_query'
description: >-
  Split-action Artifact schema type_query parameter for list_types: narrows the
  types listing by relevance, warns that a narrowed listing is not the whole
  catalog, and says to omit it when choosing a type.
ccVersion: 2.1.277
-->
list_types only: narrow the listing to the types whose title or description match this text best (case-insensitive); a type that matches less well is left out, so a narrowed listing is not the whole catalog. Omit it when choosing a type for a request, unless a listing made without it says more types exist than it shows.
