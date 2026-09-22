<!--
name: 'Tool Result: Consent Disclosure Cannot Be Displayed'
description: >-
  The `behavior:"deny"` message returned to the model when a localDisplayOnly
  permission ask cannot be forwarded because the surface cannot render the
  required consent disclosure.
ccVersion: 2.1.214
variables:
  - TOOL_RESULT_PERMISSION_DENIED_CONSENT_DISCLOSURE_UNDISPLAYABLE_VAR_0
  - TOOL_RESULT_PERMISSION_DENIED_CONSENT_DISCLOSURE_UNDISPLAYABLE_VAR_1
-->
Permission for ${TOOL_RESULT_PERMISSION_DENIED_CONSENT_DISCLOSURE_UNDISPLAYABLE_VAR_0} requires the user to read a consent disclosure before approving, and ${TOOL_RESULT_PERMISSION_DENIED_CONSENT_DISCLOSURE_UNDISPLAYABLE_VAR_1} cannot display it. Ask the user to run this from an interactive Claude Code session.
