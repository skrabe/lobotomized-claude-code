<!--
name: 'Tool Description: Computer app tools Windows capabilities note'
description: >-
  Windows-only suffix to app_* tool descriptions listing what background actions
  work in which app frameworks and what needs full control
ccVersion: 2.1.330
-->
 On Windows this works through accessibility actions and window messages to the app. In Chrome/Electron-based, Qt, classic Windows and LibreOffice apps and Thunderbird it clicks and double-clicks anywhere, types, presses keys and shortcuts, and scrolls (Thunderbird: with pagedown/pageup). In WPF apps it presses, toggles and selects listed elements, sets text fields, scrolls, and sends keys and text to whatever has keyboard focus (move it with tab). In Store/WinUI apps the same without keys. Dropdowns and menus open in Store/WinUI apps (right-click menus too) and LibreOffice. Elsewhere a dropdown is refused (its list would cover the user's work): aim app_key up/down at it or tab to it first. For a menu bar command use app_menu. Apps that list no elements (e.g. GIMP) take clicks, named keys and shortcuts, no text. These need full control: other popup menus and right-clicks, drag, hover, and in WPF and Store/WinUI apps clicks on spots that are not a listed element.
