<!--
name: 'Tool Description: app_key Windows raw input'
description: >-
  app_key Windows raw-input arm: supported keys and shortcuts by app framework,
  refused keys, password and Store app limits.
ccVersion: 2.1.330
-->
Press a key or a shortcut in one window of a granted application without bringing it to the front. It goes to whatever has keyboard focus in that window, so app_click the field or list first and check the effect with app_screenshot. Works in Chrome/Electron-based, Qt, WPF, GTK, LibreOffice and classic Windows apps and Thunderbird: return, escape, backspace, delete, tab, space, the arrow keys, home/end, page up/down and f1-f11, alone or with ctrl, shift and alt, and ctrl with a letter or digit. Refused: the clipboard shortcuts (ctrl+c, ctrl+x, ctrl+v), alt+f4, f10, alt with a letter, and the Windows key. In a password field only tab and shift+tab work. In Store/WinUI apps keys need request_full_control.
