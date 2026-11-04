<!--
name: 'Skill: /send-to-project typed message section'
description: >-
  Section of the /send-to-project prompt quoting the words the user typed in the
  field, for rewriting proposal.summary if the user declines.
ccVersion: 2.1.318
variables:
  - SKILL_SEND_TO_PROJECT_MESSAGE_TYPED_WORDS_SECTION_VAR_0
-->

## The message the user typed

The tool already holds these words and sends them as typed. They are here only so that, if the user declines the pane and says what to change, you can write the changed message in \`proposal.summary\`:

${SKILL_SEND_TO_PROJECT_MESSAGE_TYPED_WORDS_SECTION_VAR_0.message.words}
