<!--
name: 'Git bundle: inspect index link remedy'
description: >-
  Remedy fragment telling the user to check whether the git index is a link and
  remove it before running git
ccVersion: 2.1.281
-->
look at the file named index in this checkout’s git directory (in an ordinary checkout: ls -l .git/index; a link shows an arrow, ->) and, if it is a link, remove it before running any git command here, since git would write through it to whatever it points at
