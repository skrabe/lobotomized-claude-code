<!--
name: Where A Page Keeps Its State
description: >-
  Artifact-capabilities skill section telling the model whether page state
  belongs in browser storage, the artifact capability, or db.
ccVersion: 2.1.280
variables:
  - SKILL_ARTIFACT_WHERE_PAGE_KEEPS_STATE_VAR_0
  - SKILL_ARTIFACT_WHERE_PAGE_KEEPS_STATE_VAR_1
  - SKILL_ARTIFACT_WHERE_PAGE_KEEPS_STATE_VAR_2
  - SKILL_ARTIFACT_WHERE_PAGE_KEEPS_STATE_VAR_3
  - SKILL_ARTIFACT_WHERE_PAGE_KEEPS_STATE_VAR_4
-->
## Where a page keeps its state — this session

${["- A per-viewer convenience (a remembered tab, a draft): browser storage; it never reaches other viewers or Claude.",SKILL_ARTIFACT_WHERE_PAGE_KEEPS_STATE_VAR_0?"- The page itself is the record (a poll, a sign-up sheet, a checklist): the `artifact` capability — a viewer who can write republishes the whole page from its state; every open view reloads to the winner, a concurrent save rejects `conflict`, and read-only viewers cannot save. Such a page regenerates the whole document from its state: keep the head, tokens and structure and change only the content.":"",SKILL_ARTIFACT_WHERE_PAGE_KEEPS_STATE_VAR_1.includes("db")?`- Data outside the page (${SKILL_ARTIFACT_WHERE_PAGE_KEEPS_STATE_VAR_2?"Claude seeds or reads it, ":""}more than the page shows, private per viewer, many writers at once): the \`db\` capability — documents under access rules, live through \`onSnapshot\`, kept across republishes.`:"",SKILL_ARTIFACT_WHERE_PAGE_KEEPS_STATE_VAR_3].filter(SKILL_ARTIFACT_WHERE_PAGE_KEEPS_STATE_VAR_4).join(`
`)}
