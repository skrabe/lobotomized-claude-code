<!--
name: Comment reply plain-text constraint
description: >-
  Reusable constraint clause injected into the artifact comment reply/ack/edit
  composer prompts forbidding emoji and exotic spaces.
ccVersion: 2.1.232
-->
plain text only — no emoji (the posting gate rejects the invisible joiner/variation-selector code points most emoji contain), ordinary spaces only (it also rejects runs of non-breaking/ideographic spaces and braille blanks)
