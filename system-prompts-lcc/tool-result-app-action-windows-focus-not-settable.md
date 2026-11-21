<!--
name: 'Tool result: app action Windows focus not settable'
description: >-
  Windows: focus cannot be set in the background; advises app_click for
  Chrome/Electron/Qt/classic apps and tab keys for WPF.
ccVersion: 2.1.330
-->
on Windows keyboard focus cannot be set directly in the background (doing so would bring the app to the front), so nothing was done. In Chrome/Electron-based, Qt and classic Windows apps app_click the element instead: the click moves the focus there. In a WPF app move it with app_key tab or shift+tab
