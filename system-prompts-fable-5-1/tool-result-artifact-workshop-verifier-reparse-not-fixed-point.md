<!--
name: 'Workshop Verifier: Reparse Not Fixed Point'
description: >-
  Document-level verifier refusal returned when the page serializes to different
  bytes on a second parse/serialize round.
ccVersion: 2.1.219
-->
The page serializes to different bytes on a second parse→serialize round, so each decision confirm would keep rewriting it — this indicates parser/serializer-divergent markup; simplify the construct at the quoted position.
