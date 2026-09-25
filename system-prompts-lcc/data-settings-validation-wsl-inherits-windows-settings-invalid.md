<!--
name: 'Data: Settings Validation wslInheritsWindowsSettings Invalid'
description: >-
  Settings validation issue when wslInheritsWindowsSettings is present but not a
  boolean: the source's WSL opt-in cannot be read and WSL fails it closed until
  fixed.
ccVersion: 2.1.282
-->
"wslInheritsWindowsSettings" was present but invalid (it takes true or false), so this source's WSL opt-in cannot be read until it is fixed. WSL fails it closed: in an administrator source it arms the Windows policy chain with no user-writable source (/etc/claude-code, HKCU) read beneath it; in HKCU it leaves HKCU unapplied.
