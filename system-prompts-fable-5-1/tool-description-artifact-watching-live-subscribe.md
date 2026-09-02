<!--
name: 'Tool Description: Artifact Watching Live Subscribe'
description: >-
  Interactive-session Artifact watching section: publishing starts a live
  subscription and only the main loop holds a watch.
ccVersion: 2.1.257
variables:
  - TOOL_DESCRIPTION_ARTIFACT_WATCHING_LIVE_SUBSCRIBE_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_WATCHING_LIVE_SUBSCRIBE_VAR_1
-->
**Watching for republishes**: publishing subscribes this session to the artifact's live changes (\`status\` shows whether it connected); \`action: "watch"\` with a \`url\` watches one you did not just publish. A republish from elsewhere arrives as a notification: re-read before editing.${TOOL_DESCRIPTION_ARTIFACT_WATCHING_LIVE_SUBSCRIBE_VAR_0?' A comment on a watched artifact that is sent to Claude also wakes this session, but only while that artifact\'s `status` row says auto-replies armed (when comment auto-replies are on for this session, a publish arms those, and so does `action: "watch"` on an artifact the user can edit whose link the user gave in their own message — never on one the user can only view); plain comments never notify this session — read them with `action: "comments"` when the user asks.':TOOL_DESCRIPTION_ARTIFACT_WATCHING_LIVE_SUBSCRIBE_VAR_1} ${TOOL_DESCRIPTION_ARTIFACT_WATCHING_LIVE_SUBSCRIBE_VAR_0?"After a `--resume` or `--continue` in an interactive terminal, the watch on the artifact this session most recently published or read usually comes back, along with every watch that was replying to comments (replying again, unless the user had stopped it); other clients may restore nothing. `status` shows what is armed.":"After a `--resume` or `--continue` in an interactive terminal, the watch on the artifact this session most recently published or read usually comes back; other clients may restore nothing. `status` shows what is armed."} Claim a watch only when a watch result, \`status\`, or a publish result's "already connected" line says so.
