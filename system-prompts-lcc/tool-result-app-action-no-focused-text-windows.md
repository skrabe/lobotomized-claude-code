<!--
name: 'App action: no focused text (Windows)'
description: >-
  Refusal: nothing typed, no settable text field; click or tab to the field
  (WPF/WinUI notes).
ccVersion: 2.1.330
-->
nothing was typed: there is no text field here that can be set directly, and no editable element holds the app's keyboard focus where this text was aimed. app_click the place the text should go and retry (in a WPF app a click moves no focus: use app_key tab until the field has it, then app_type with no coordinate). In Store/WinUI apps only standard text fields can be filled
