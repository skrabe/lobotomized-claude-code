# Prompt-size measurements

Measured on 4 November 2026 with Claude Code 2.1.317, [LCC `7c35504e`](https://github.com/skrabe/lobotomized-claude-code/tree/7c35504e77cabaae3660966b846d008ac8bec0f5) and [tweakcc `13b46f57`](https://github.com/skrabe/tweakcc-fixed/tree/13b46f57e1392386db48040808db842a3532e269).

## Captured Opus request

| Unicode characters          |  Stock | Shared LCC + tweakcc defaults | Change |
| --------------------------- | -----: | ----------------------------: | -----: |
| System blocks               |  3,820 |                         2,852 | −25.3% |
| Top-level tool descriptions |  8,308 |                         6,540 | −21.3% |
| Combined                    | 12,128 |                         9,392 | −22.6% |

[Machine-readable results](prompt-size-2.1.317.json) include binary hashes, per-tool sizes and the schema comparison hash.

The fixture used native Opus 5.5 routing, medium effort and a single `Reply with exactly PONG.` turn. Two copies of the same pristine native binary were compared. One copy received shared LCC prompts and reminders through tweakcc with a fresh default config. FFF and the Fable/Mythos all-models switch were off.

Each process used an isolated Claude profile, a working directory outside the user's home, and no global CLAUDE.md, private overlay, plugins or MCP servers. The API base URL pointed at a localhost server that captured the actual assembled request and returned synthetic SSE text. No request was forwarded to a model provider. A `PONG` response verifies the capture path, not model behavior.

The offered schema entries were `Agent`, `Bash`, `Edit`, `Glob`, `Grep`, `Read`, `Skill`, `DeferredToolPlaceholder` and `Write`. Their order and input-schema structure matched. The structure hash excludes `description` and `title` fields.

Counts sum decoded system-block strings and top-level tool descriptions, without inserted separators. They exclude input schemas, parameter descriptions, conversation messages, metadata and later tool results. They are not token counts, cost estimates, speed measurements or task-quality scores. Different models, features, toolsets, dates and paths can change the result.

## Catalogue inventory

The 2.1.317 catalogue contains 16,355 sites across 15,141 IDs. The shared directory has files for 15,136 of those IDs:

| File classification                                                            |    IDs |
| ------------------------------------------------------------------------------ | -----: |
| Nonempty rewrite                                                               |    835 |
| Empty override of nonempty stock text                                          |    202 |
| Matches a stock variant after template unescaping and whitespace normalization | 14,099 |

Five catalogue IDs have no override file and retain stock text. Another 38 files have no matching ID in this catalogue and contribute nothing to this projection.

The [catalogue data](catalogue-2.1.317.json) also projects the text at every catalogued site: 8,642,650 stock characters and 8,368,570 with shared overrides, a 3.17% reduction. Large bundled references dominate that total. Many are loaded only when requested; the total is not a session's context size.

Derivation uses tweakcc's `tools/lib/auditCorpus.mjs`: `parseOverrideFile`, `reconstructPristine` and `unescapeDeployed`. A file counts as stock if it matches any variant of its ID. The projection counts every catalogue occurrence, substitutes an override where present and leaves symbolic runtime interpolations unresolved. HTML metadata is excluded. This inventory is separate from the captured-request measurement above.

## Reproducing a request capture

Requires Python 3.9+, Claude Code 2.1.317 and a built checkout of tweakcc. Use the pinned commits above for the recorded source state. No API key is needed.

Create a temporary directory outside your projects. Copy the pristine Claude binary into it twice as `stock-claude` and `lcc-claude`; don't point the fixture at your installed binary. In a fresh tweakcc config directory, copy this repository's `system-prompts-lcc/` to `system-prompts/` and `system-reminders/` to `system-reminders/`. Leave the config absent so tweakcc creates its defaults.

Apply to the throwaway LCC copy from the tweakcc checkout, substituting your temporary paths:

```sh
TWEAKCC_CONFIG_DIR=/tmp/lcc-measure/tweakcc \
TWEAKCC_CC_INSTALLATION_PATH=/tmp/lcc-measure/lcc-claude \
node dist/index.mjs --apply
```

Then run from the LCC checkout:

```sh
python3 tools/measure-prompt-text.py \
  --stock /tmp/lcc-measure/stock-claude \
  --patched /tmp/lcc-measure/lcc-claude \
  --out /tmp/lcc-measure/result.json
```

The [script](../tools/measure-prompt-text.py) creates a temporary home and profile, uses a fake local key, starts a localhost SSE fixture, and checks that tool names and schema structure match. Its JSON output contains counts and hashes only. The recorded results were reproduced with this script against the same two binary copies. It doesn't remove personal instructions already compiled into a binary, so prepare the LCC copy from shared files as above.
