<!--
name: 'Slash command: plugin validate code ambiguous slash'
description: >-
  Reports a slash read as division by one reader and regex by the other, and how
  to disambiguate it
ccVersion: 2.1.328
-->
a "/" that the scan reads one way and the JavaScript engine another (a division or the start of a regular expression), so the scan cannot tell what this file runs: end the statements around it with ";", and if it is a division, put the expression in parentheses
