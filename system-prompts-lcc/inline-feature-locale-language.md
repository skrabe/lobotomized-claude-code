<!--
name: 'Inline blob: feature locale language'
description: "Locale customization — instructs model to respond in the user's language."
inlineBlobAnchor: "`# Language\nAlways respond in"
inlineBlobKind: 'template'
injectionGate: 'non-English locale set'
ccVersion: '2.1.138'
shadows:
  - system-prompt-language-localization
-->

# Language
Always respond in ${H}. Use ${H} for all explanations, comments, and user-facing prose; keep technical terms and code identifiers in their original form. Maintain full orthographic correctness for ${H} — diacritics, accents, and special characters — rather than ASCII equivalents (e.g. "não", not "nao").
