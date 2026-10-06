<!--
name: 'Tool Result: Git bundle gitattributes unreadable retry'
description: >-
  Git bundle upload refusal when HEAD's .gitattributes rules could not be read
  reliably: retry, then save each committed .gitattributes as plain UTF-8
  without BOM, commit all changes, or check git fsck.
ccVersion: 2.1.291
-->
HEAD's .gitattributes rules could not be read reliably: retry first. If it stops here again, save each committed .gitattributes above a changed file as plain UTF-8 text with no byte-order mark (one saved as UTF-16 stops it, for example, and so does one that git lists as a submodule) and commit that; or commit all your changes; or check the repository's objects (git fsck).
