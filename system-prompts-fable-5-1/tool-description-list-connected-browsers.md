<!--
name: 'Tool Description: list_connected_browsers'
description: >-
  list_connected_browsers tool description (lists connected Chrome extension
  instances).
ccVersion: 2.1.274
-->
List all Chrome browsers (extension instances) currently connected to this account. Returns each browser's deviceId, display name, OS platform, isLocal (its OS matches this computer's, a weak hint), when known onThisComputer (it is, or recently was, running on this computer), and inUse on the browser this session's actions go to when that is settled. When the user needs to choose a browser, use this to present the choices before select_browser.
