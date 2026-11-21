<!--
name: 'API Error: No usable login under device policy'
description: >-
  Authentication-failed API error when the hybrid login yields to device policy,
  explaining why remote managed settings make the session ineligible and
  pointing to /login.
ccVersion: 2.1.330
variables:
  - DATA_API_ERROR_NO_USABLE_LOGIN_DEVICE_POLICY_VAR_0
  - DATA_API_ERROR_NO_USABLE_LOGIN_DEVICE_POLICY_VAR_1
-->
This session has no login that it can use, and ${DATA_API_ERROR_NO_USABLE_LOGIN_DEVICE_POLICY_VAR_0.describeRemoteManagedSettingsIneligibleReason(DATA_API_ERROR_NO_USABLE_LOGIN_DEVICE_POLICY_VAR_1)} To use an account of your own, run /login.
