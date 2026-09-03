<!--
name: Audio File Transcription Note
description: >-
  Model-facing context note injected when the user @-mentions an audio file,
  telling the model the file was transcribed by Anthropic's speech-to-text and
  to treat the transcript as the spoken content.
ccVersion: 2.1.234
variables:
  - SYSTEM_PROMPT_AUDIO_FILE_TRANSCRIPTION_NOTE_VAR_0
  - SYSTEM_PROMPT_AUDIO_FILE_TRANSCRIPTION_NOTE_VAR_1
-->
The user @-mentioned the audio file ${SYSTEM_PROMPT_AUDIO_FILE_TRANSCRIPTION_NOTE_VAR_0(SYSTEM_PROMPT_AUDIO_FILE_TRANSCRIPTION_NOTE_VAR_1.filename)}. Claude Code transcribed it with Anthropic's speech-to-text service before sending this message. The transcript below IS the spoken content of that file — rely on it as you would on the output of a file-read tool; you do not need a separate tool to hear the audio.
