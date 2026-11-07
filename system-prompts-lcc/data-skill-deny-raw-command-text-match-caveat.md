<!--
name: 'Data: skill deny raw command text match caveat'
description: >-
  Caveat that a skill's deny fragments match the command text, so message, body
  or path text containing a fragment trips it too and should be reworded
ccVersion: 2.1.319
-->
The match is on the command text, with quotes resolved on Bash (case-insensitive in PowerShell, so a lowercase short flag can trip an uppercase one), so message, body or path text that merely contains one of these fragments trips it too; reword that text if so.
