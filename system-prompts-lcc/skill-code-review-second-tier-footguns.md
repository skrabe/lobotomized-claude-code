<!--
name: Code review second tier footguns
description: Lists subtle defect classes for deeper code review passes.
ccVersion: 2.1.294
-->
moved/extracted code that dropped a guard
or anchor; second-tier footguns (dataclass default evaluated once, \`hash()\`
non-determinism, lock-scope shrink, predicate methods with side effects);
setup/teardown asymmetry in tests; config defaults flipped.
