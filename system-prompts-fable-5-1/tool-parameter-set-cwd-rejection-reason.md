<!--
name: Set Cwd Rejection Reason Field
description: >-
  Description of the reason enum in the set_cwd rejected-status output schema
  (W_C) explaining the unsafe_path reason, delivered to the model as tool-result
  schema; model-facing.
ccVersion: 2.1.201
-->
unsafe_path: the target's canonical path contains characters that do not render as visible, space-distinguishable glyphs — control (Cc), format (Cf), default-ignorable, line/paragraph-separator (Zl/Zp), non-ASCII-space Zs, or braille-blank code points; rejected fail-closed before the trust round-trip, and the offending path is never echoed back.
