<!--
name: 'Skill: Code Review (Angle D — language-pitfall specialist)'
description: >-
  The language-pitfall finder angle of the code-review skill — scan for the
  classic pitfalls of the diff's language/framework
ccVersion: 2.1.160
-->
### Angle D — language-pitfall specialist

Identify the diff's language/framework, then scan for its classic idiom traps —
the ones a generic line-scan misses because the code looks correct. JS:
falsy-zero, \`==\` coercion, closure-captured loop var, \`async\` map without
\`await\`. Python: mutable default args, late-binding closures, integer/float
division. Go: nil-map write, range-var capture, unchecked error shadowing. Plus
cross-language: SQL/shell injection on interpolated input, timezone/DST drift,
float equality, off-by-one on inclusive vs exclusive bounds. For each instance
the diff introduces, name the input or state that triggers it — that's a
candidate.
