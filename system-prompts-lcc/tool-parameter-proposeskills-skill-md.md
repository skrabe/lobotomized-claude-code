<!--
name: 'Tool Parameter: ProposeSkills skillMd'
description: >-
  zod .describe() for the ProposeSkills tool's per-proposal skillMd field,
  instructing the model to supply a complete SKILL.md draft
ccVersion: 2.1.257
-->
The complete SKILL.md exactly as it should be saved: frontmatter plus the full body. When the user saves, the body below the frontmatter becomes the skill's entire instructions and the name and description come from the fields above; other frontmatter keys are not kept. For an improvement this replaces the existing skill's SKILL.md entirely, so read that skill's current SKILL.md first and include everything worth keeping, not only the changes.
