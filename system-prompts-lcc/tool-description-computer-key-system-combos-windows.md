<!--
name: 'Tool description: key system combos (Windows)'
description: >-
  Windows suffix of key tool description: system combos and registered hotkeys
  need systemKeyCombos grant.
ccVersion: 2.1.332
-->
System-level combos (quit app, switch app, lock screen), and any key or Ctrl, Alt or Shift combination another program has registered as a system-wide hotkey, require the `systemKeyCombos` grant. Without it they return an error. The shortcuts for voice typing, Voice Access, Live Captions and Game Bar's microphone are always refused.
