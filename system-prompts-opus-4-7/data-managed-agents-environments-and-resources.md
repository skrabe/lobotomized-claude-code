<!--
name: 'Data: Managed Agents environments and resources'
description: >-
  Reference documentation covering Managed Agents environments, file resources,
  GitHub repository mounting, and the Files API with SDK examples
ccVersion: 2.1.237
-->
# Managed Agents — Environments & Resources

## Environments

Creating a session requires an \`environment_id\`.

**Environment names must be unique.** Creating an environment with an existing name returns 409.

### Networking

| Network Policy   | Description                                                   |
| ---------------- | ------------------------------------------------------------- |
| \`unrestricted\`   | Full egress (except legal blocklist)                          |
| \`limited\`        | Deny-by-default; opt in via \`allowed_hosts\` / \`allow_package_managers\` / \`allow_mcp_servers\` |

All three \`limited\` fields are optional. \`allow_package_managers\` (default \`false\`) permits PyPI/npm/etc.; \`allow_mcp_servers\` (default \`false\`) permits the agent's configured MCP server endpoints without listing them in \`allowed_hosts\`.

**MCP caveat:** Under \`limited\` networking, either set \`allow_mcp_servers: true\` or add each MCP server domain to \`allowed_hosts\`. Otherwise the container can't reach them and tools silently fail.

### Creating an environment

The SDK adds \`managed-agents-2026-04-01\` automatically. TypeScript: \`client.beta.environments.create({ name, config })\`.

### Environment CRUD

| Operation        | Method   | Path                                       | Notes |
| ---------------- | -------- | ------------------------------------------ | ----- |
| List             | \`GET\`    | \`/v1/environments\`                         | Paginated (\`limit\`, \`after_id\`, \`before_id\`) |

Changes apply only to **new** containers; existing sessions keep their original config.

---

## Resources

Resources are resolved during session creation, so a bad \`file_id\` or an unreachable repo surfaces on the create call rather than mid-run. Max **999 file resources** per session.

### File Uploads (input — host → agent)

Upload a file first via the Files API, then reference by \`file_id\` + \`mount_path\`:

\`\`\`ts
// 1. Upload
const file = await client.beta.files.upload({
  file: fs.createReadStream("data.csv"),
  purpose: "agent",
});

// 2. Attach as a session resource
const session = await client.beta.sessions.create({
  agent: agent.id,
  environment_id: envId,
  resources: [
    { type: "file", file_id: file.id, mount_path: "/workspace/data.csv" }
  ],
});
\`\`\`

**\`mount_path\` is required** and must be absolute. Parent directories are created automatically. Agent working directory defaults to \`/workspace\`. Files are mounted read-only — the agent writes modified versions to new paths.

### Session outputs (output — agent → host)

The agent can write files to \`/mnt/session/outputs/\` during a session. These are automatically captured by the Files API and can be listed and downloaded afterwards:

**Requirements:**
- The \`write\` tool (or \`bash\`) must be enabled for the agent to create output files.
- Session-scoped \`files.list\` / \`files.download\` captures outputs written to \`/mnt/session/outputs/\`.
- The filter parameter is **\`scope_id\`** (REST query param \`?scope_id=<session_id>\`). The SDK's files resource auto-adds only the \`files-api-2025-04-14\` header, so pass \`betas: ["managed-agents-2026-04-01"]\` explicitly (or both headers on raw HTTP) — without it the API may reject \`scope_id\` as an unknown field. Requires \`@anthropic-ai/sdk\` ≥ 0.88.0 / \`anthropic\` (Python) ≥ 0.92.0 — older versions don't type \`scope_id\`. The \`ant\` CLI does **not** expose this flag yet; use the SDK or curl.
- Pass the session ID returned by \`sessions.create()\` verbatim (e.g. \`sesn_011CZx...\`) — the API validates the prefix.
- There's a brief indexing lag (~1–3s) between \`session.status_idle\` and output files appearing in \`files.list\`. Retry once or twice if empty.

> **Fallback when \`scope_id\` filtering is unavailable** (older SDK, or endpoint returns an error): send a follow-up \`user.message\` asking the agent to \`read\` each file under \`/mnt/session/outputs/\` and return the contents. The agent streams the file bodies back as \`agent.message\` text. This works for text files only and costs output tokens — use it to unblock, not as the primary path.

### GitHub Repositories

Clones a GitHub repository into the session container during initialization, before the agent begins execution. The agent can read, edit, commit, and push via \`bash\` (\`git\`). Multiple repositories per session are supported — add one \`resources\` entry per repo. Repositories are cached, so future sessions that use the same repository start faster.

Repositories are attached for the lifetime of the session — to change which repositories are mounted, create a new session. You **can** rotate a repository's \`authorization_token\` on a running session via \`client.beta.sessions.resources.update(resource_id, {session_id, authorization_token})\`; the resource \`id\` is returned at session creation and by \`resources.list()\`.

**Fields:**

| Field | Required | Notes |
|---|---|---|
| \`type\` | ✅ | \`"github_repository"\` |
| \`url\` | ✅ | The GitHub repository URL |
| \`authorization_token\` | ✅ | GitHub Personal Access Token with repository access. **Never echoed in API responses.** |
| \`mount_path\` | ❌ | Path where the repository will be cloned. Defaults to \`/workspace/<repo-name>\`. |
| \`checkout\` | ❌ | \`{type: "branch", name: "..."}\` or \`{type: "commit", sha: "..."}\`. Defaults to the repo's default branch. |

**Token permission levels** (fine-grained PATs):
- \`Contents: Read\` — clone only
- \`Contents: Read and write\` — push changes and create pull requests

> ⚠️ **To generate pull requests** you also need GitHub **MCP server** access — the \`github_repository\` resource gives filesystem + git access only. See \`shared/managed-agents-tools.md\` → MCP Servers. The PR workflow is: edit files in the mounted repo → push branch via \`bash\` (authenticated via the git proxy using \`authorization_token\`) → create PR via the MCP \`create_pull_request\` tool (authenticated via the vault).

---

## Files API

The \`scope_id\` filter on List scopes the results to files written to \`/mnt/session/outputs/\` by that session. Without the filter, you get all files uploaded to your account.
