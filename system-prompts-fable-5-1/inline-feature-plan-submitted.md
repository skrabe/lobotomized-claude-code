<!--
name: 'Inline blob: feature plan submitted'
description: 'Plan-mode submission acknowledgment when subagent submits plan to team lead.'
inlineBlobAnchor: "`Your plan has been submitted to the team lead for approval\\."
inlineBlobKind: 'template'
injectionGate: 'plan-mode submission to team lead (subagent context)'
ccVersion: '2.1.138'
shadows:
  - system-reminder-team-plan-submitted
-->

Your plan has been submitted to the team lead for approval.

Plan file: ${q}

Wait for approval before implementing; the decision arrives in your inbox. If rejected, refine the plan based on the feedback.

Request ID: ${z}
