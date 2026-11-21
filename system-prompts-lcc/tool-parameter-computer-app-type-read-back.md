<!--
name: 'Tool Parameter: Computer app_type read_back'
description: >-
  read_back parameter: return changed text read from the field, limits and
  exclusions
ccVersion: 2.1.330
variables:
  - TOOL_PARAMETER_COMPUTER_APP_TYPE_READ_BACK_VAR_0
-->
Also return what this call changed, read from the field afterwards: the changed part with up to 40 characters of the text either side of it (none after replace_text), 500 characters at most. Shows what the app made of the text (autocorrect, formatting, a caret that was elsewhere) without a screenshot. Never returned for password or secret-looking fields or in file dialogs; where a field can't be read, the result says so. \`text\` may then have at most ${TOOL_PARAMETER_COMPUTER_APP_TYPE_READ_BACK_VAR_0} characters.
