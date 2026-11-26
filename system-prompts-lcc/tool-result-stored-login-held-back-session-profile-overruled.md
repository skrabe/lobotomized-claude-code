<!--
name: 'Stored login held back: profile overruled'
description: >-
  Error that nothing was sent because a key, token or provider set since the
  session began would replace its sign-in.
ccVersion: 2.1.332
-->
Nothing was sent: a key, token, or provider set since this session began would replace its sign-in. It may come from the "env" block of a settings file (/status shows what is in use, but not a key set in ANTHROPIC_CUSTOM_HEADERS). Remove it, then send again. If this session still sends nothing, exit and run claude --resume. A new session would use it too, so remove it before you reopen this session.
