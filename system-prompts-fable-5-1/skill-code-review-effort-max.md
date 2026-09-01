<!--
name: 'Skill: Code Review (xhigh effort, inline single-pass)'
description: >-
  Effort-tier prompt for the inline xhigh code review — 10 angles run in-context
  with no subagents, dedup only (no verify), sweep, up to 15 findings. Reshaped
  in 2.1.214; the fan-out variant now lives in skill-code-review-effort-max-3.
ccVersion: 2.1.218
variables:
  - EFFORT_LEVEL
  - PHASE_0_GATHER_DIFF
  - AGENT_TOOL_NAME
  - HIGH_EFFORT_ANGLES
  - ANGLE_REUSE
  - ANGLE_SIMPLIFICATION
  - ANGLE_EFFICIENCY
  - ANGLE_ALTITUDE
  - ANGLE_CONVENTIONS
  - CLEANUP_CANDIDATES_NOTE
-->
\`xhigh effort → 10 inline angles → dedup (no verify) → sweep → ≤15 findings\`

You are reviewing for **recall** at extra-high effort: catch every real bug. At
this level, catching real bugs matters more than avoiding false positives — a
missed bug ships. Err on the side of surfacing.

${EFFORT_LEVEL}
## Phase 1 — Find candidates (5 correctness angles + 3 cleanup angles + 1 altitude angle + 1 conventions angle, up to 8 each)

Run **10 independent finder angles** in sequence yourself, in this context — spawn no subagents for them. Each
surfaces **up to 8 candidate findings**. Don't let one angle's conclusions
suppress another's — if two angles flag the same line for different reasons,
record both.

${PHASE_0_GATHER_DIFF}
### Angle D — language-pitfall specialist

Scan for the classic pitfalls of the diff's language/framework — for example:
JS falsy-zero, \`==\` coercion, closure-captured loop var; Python mutable default
args, late-binding closures; Go nil-map write, range-var capture; SQL injection;
timezone/DST drift; float equality. Flag any instance the diff introduces.

### Angle E — wrapper/proxy correctness

When the PR adds or modifies a type that wraps another (cache, proxy, decorator,
adapter): check that every method routes to the wrapped instance and not back
through a registry/session/global — e.g. a caching provider holding a
\`delegate\` field that resolves IDs via \`session.get(...)\` instead of
\`delegate.get(...)\` will re-enter the cache or recurse. Also check that the
wrapper forwards all the methods the callers actually use.

${AGENT_TOOL_NAME}
${HIGH_EFFORT_ANGLES}
${ANGLE_REUSE}
${ANGLE_SIMPLIFICATION}
${ANGLE_EFFICIENCY}
${ANGLE_ALTITUDE}
## Phase 2 — Dedup only (no verify)

Pool all candidates. Dedup near-duplicates only (same defect, same location, same reason → keep one). Skip the verifiers and leave each candidate's judgment as it stands. Sort by severity. Keep the ones you're uncertain about.

## Phase 3 — Sweep for gaps

Take one more pass (same context — no subagent) as a fresh reviewer who has the deduplicated list. Re-read
the diff and enclosing functions looking only for defects not already listed —
the job is gaps, so leave what's already there alone. Focus
on what the first pass tends to miss: moved/extracted code that dropped a guard
or anchor; second-tier footguns (dataclass default evaluated once, \`hash()\`
non-determinism, lock-scope shrink, predicate methods with side effects);
setup/teardown asymmetry in tests; config defaults flipped.

Surface **up to 8 additional candidates**, each naming a defect not already on
the list. If nothing new, return nothing from this phase.

${ANGLE_CONVENTIONS(CLEANUP_CANDIDATES_NOTE)(15)}
