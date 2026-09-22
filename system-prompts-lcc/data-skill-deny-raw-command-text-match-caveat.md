<!--
name: 'Data: Skill Deny Raw Command Text Match Caveat'
description: >-
  Shared caveat that skill deny matching is on raw command text, interpolated
  into skill permission-deny suffixes.
ccVersion: 2.1.273
-->
The match is on the raw command text (case-insensitive in PowerShell, so a lowercase short flag can trip an uppercase one), so message, body or path text that merely contains one of these fragments trips it too; reword that text if so.
