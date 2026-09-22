<!--
name: 'System Reminder: Skill scoped-variants guidance'
description: >-
  Appended when invoking an unscoped skill that has directory-scoped variants,
  nudging Claude to invoke the matching variant
ccVersion: 2.1.204
variables:
  - SYSTEM_REMINDER_SKILL_SCOPED_VARIANTS_GUIDANCE_VAR_0
-->
The bare name always resolves to this unscoped skill; the variants are reachable only by their exact qualified names. If the files you are working on are under a variant's directory, invoke that variant now with the ${SYSTEM_REMINDER_SKILL_SCOPED_VARIANTS_GUIDANCE_VAR_0} tool and follow it instead — it carries that subtree's own instructions. If your changes span more than one variant's directory, run each matching variant.
