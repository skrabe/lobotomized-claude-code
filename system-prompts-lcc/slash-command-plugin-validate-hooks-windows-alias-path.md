<!--
name: '/plugin validate: Windows alias path'
description: >-
  /plugin validate error that a hooks path can be opened by Windows as another
  file, listing the spellings to avoid.
ccVersion: 2.1.326
-->
Windows can open this path as another file, so hooks can load that are not listed here. Spell it without a backslash, a colon, a name ending in a dot or a space, or a short name such as NAME~1.
