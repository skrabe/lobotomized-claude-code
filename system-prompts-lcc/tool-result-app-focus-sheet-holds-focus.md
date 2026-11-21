<!--
name: 'App focus: sheet holds focus'
description: >-
  Refusal for app_focus: a sheet/system panel holds focus or contains target;
  dismiss and retry.
ccVersion: 2.1.330
-->
a dialog sheet or system panel (Open/Save or similar) is up in this app, and either it holds the keyboard focus or the element you aimed at is inside it, so focus was NOT moved. app_focus stays out of sheets and of a system panel that holds the focus: finish or dismiss it (or ask the user to) and then retry
