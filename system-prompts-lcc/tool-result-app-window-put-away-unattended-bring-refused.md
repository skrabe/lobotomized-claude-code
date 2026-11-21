<!--
name: 'App window put away: unattended bring refused'
description: >-
  kn arm for bring+unattended: app_bring_to_current_space needs approval;
  continue elsewhere and report.
ccVersion: 2.1.330
-->
Only app_bring_to_current_space brings it back, and that needs a person's approval: this run is unattended, so it is refused unless the approval was given earlier for this task's scheduled runs. app_screenshot and app_list_windows still work on the window; otherwise continue with another window or app, and report in your result that this one was put away
