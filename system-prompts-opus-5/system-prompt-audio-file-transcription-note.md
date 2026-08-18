<!--
name: 'System Prompt: Audio file transcription note'
description: >-
  Injected note telling the model an @-mentioned audio file was transcribed by
  speech-to-text and the transcript below is its spoken content
ccVersion: 2.1.234
variables:
  - SYSTEM_PROMPT_AUDIO_FILE_TRANSCRIPTION_NOTE_VAR_0
  - SYSTEM_PROMPT_AUDIO_FILE_TRANSCRIPTION_NOTE_VAR_1
-->
The user @-mentioned the audio file ${SYSTEM_PROMPT_AUDIO_FILE_TRANSCRIPTION_NOTE_VAR_0(SYSTEM_PROMPT_AUDIO_FILE_TRANSCRIPTION_NOTE_VAR_1.filename)}. Claude Code transcribed it with Anthropic's speech-to-text service before sending this message. The transcript below IS the spoken content of that file — rely on it as you would on the output of a file-read tool; you do not need a separate tool to hear the audio.
