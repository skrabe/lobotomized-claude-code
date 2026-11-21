<!--
name: 'Tool Description: app_list_windows'
description: app_list_windows tool description
ccVersion: 2.1.330
-->
List the windows of one granted application. Returns [{window_id, title, is_main, is_minimized, is_hidden, is_off_space, bounds}]. is_hidden means the whole app is hidden. Dialogs and palettes the app does not report as regular windows carry is_auxiliary: true; use their window_id like any other window's, but the element list app_screenshot returns for them may be empty. Use the window_id with app_screenshot and the app_* action tools.
