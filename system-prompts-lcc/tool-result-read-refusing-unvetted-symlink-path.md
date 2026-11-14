<!--
name: 'Tool Result: Read refused for unvetted symlink path'
description: >-
  Error telling Claude a file read was refused because a symlink on its path may
  lead outside the checked folder or the link chain is too long, and to replace
  the link with a regular folder or file
ccVersion: 2.1.325
-->
Refusing to read a file whose path could not be vetted: a symbolic link on its path has a target that may lead to a different folder than the one that was checked (such as a target that is not valid UTF-8, or, on Windows, one with ".." after a folder name), or the path runs through too many links. Replace that link, or the chain of links, with a regular folder or file.
