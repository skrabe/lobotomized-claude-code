<!--
name: Artifact Reply Text Contains Invisible Characters
description: >-
  validateInput failure (errorCode 11) rejecting reply text that carries
  zero-width/bidi/variation code points or exotic blanks, and telling Claude to
  resend as plain ASCII-spaced text without emoji.
ccVersion: 2.1.221
-->

text contains invisible or control characters (zero-width, bidi, variation/tag code points) or a run of exotic blanks (non-breaking/ideographic spaces, braille blanks — with or without plain spaces between them) — note this includes the joiner/variation-selector code points inside most emoji; resend the reply as plain text without emoji, using ordinary spaces only
