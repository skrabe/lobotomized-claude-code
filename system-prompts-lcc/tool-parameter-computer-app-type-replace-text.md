<!--
name: 'Tool Parameter: Computer app_type replace_text'
description: >-
  replace_text parameter: replace one exact piece of field text, limits and
  refusals
ccVersion: 2.1.330
variables:
  - TOOL_PARAMETER_COMPUTER_APP_TYPE_REPLACE_TEXT_VAR_0
-->
Replace this piece of the field's text with \`text\` and leave the rest as it is, also where the piece is scrolled out of view. It must occur exactly once in the field, matched exactly (capitals, spaces, punctuation). If it doesn't, or the field is a password or secret-looking field, is in a file dialog or can't be searched, no text is changed and the error says why. An empty \`text\` removes the piece; a few kinds of field refuse that. \`text\` and replace_text: at most ${TOOL_PARAMETER_COMPUTER_APP_TYPE_REPLACE_TEXT_VAR_0} characters each. Not together with overwrite_existing or mode: "replace".
