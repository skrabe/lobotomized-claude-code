<!--
name: 'Steward watch: official plugin to-watch steps'
description: >-
  Steps for watching when the official plugin is held by the checkout: remove
  its marketplace declaration, move its folder, and reinstall at user scope.
ccVersion: 2.1.331
variables:
  - DATA_STEWARD_WATCH_CHECKOUT_PLUGIN_TO_WATCH_OFFICIAL_VAR_0
  - DATA_STEWARD_WATCH_CHECKOUT_PLUGIN_TO_WATCH_OFFICIAL_VAR_1
-->
To watch: (1) If the settings of this checkout or of an --add-dir folder declare this plugin's marketplace, take it out of them. (2) If the plugin's folder lies inside the checkout or a folder added with --add-dir, move it out. ${DATA_STEWARD_WATCH_CHECKOUT_PLUGIN_TO_WATCH_OFFICIAL_VAR_0("userSettings")?`(3) From outside any checkout: first check in /plugin's Marketplaces tab that the row claude-plugins-official names the GitHub repository anthropics/claude-plugins-official (the tab shows no branch or path). If it names another, don't install. Then, if the plugin isn't installed for you at user scope, run /plugin install ${DATA_STEWARD_WATCH_CHECKOUT_PLUGIN_TO_WATCH_OFFICIAL_VAR_1} and pick "Install for you (user scope)", which takes the plugin anew from that repository. If it is installed, but switched off, switch it on in /plugin. Then start Claude Code again in this checkout (don't resume a session). Installing it checks nothing that is named above, and if this project has an install of another version, that one still loads here`:"(3) This session doesn't read your own settings (as with --setting-sources without user), so an install for you changes nothing here. Start a session that reads them, and run the command again"}
