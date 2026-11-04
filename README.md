<p align="center">
  <img src="./assets/banner.png" alt="lobotomized-claude-code" width="420">
</p>

# lobotomized-claude-code

Shorter system prompts and tool descriptions for Claude Code. Applied with [tweakcc-fixed](https://github.com/skrabe/tweakcc-fixed).

Tested on Claude Code 2.1.317 with Opus 5.5 and Fable 5.1.

[Install](#install) · [Measured size](#measured-size) · [Files](#files) · [Editing](#editing)

## What changes

- Shorter Agent, Skill, shell and scheduling instructions.
- Fewer repeated cautions, completion nags and offers to use unrelated features.
- Tool arguments, result formats and instructions for optional features stay documented.
- Reference fixes for batch results, tool examples and context limits.

The shared set has 835 rewritten fragments and 202 empty overrides in the 2.1.317 catalogue. Another 14,099 match stock. Claude Code loads fragments according to the model, tools and features in use.

## Measured size

A clean Opus 5.5 fixture sent 22.6% less system and tool-description text:

| Text              |  Stock | LCC + tweakcc main | Change |
| ----------------- | -----: | -----------------: | -----: |
| System blocks     |  3,820 |              2,852 | −25.3% |
| Tool descriptions |  8,308 |              6,540 | −21.3% |
| Combined          | 12,128 |              9,392 | −22.6% |

Counts are Unicode characters from captured requests on 4 November 2026. The fixture used nine tool-schema entries, default patcher settings, and no private overlay, global CLAUDE.md, plugins or MCP servers. Schemas and conversation messages add to these totals. [Method, data and reproduction](docs/measurements.md).

## Install

For a fresh setup where `~/.tweakcc/system-prompts` and `system-reminders` don't already exist:

```sh
(
  set -e
  test ! -e ~/.tweakcc/system-prompts
  test ! -e ~/.tweakcc/system-reminders
  git clone https://github.com/skrabe/lobotomized-claude-code ~/.tweakcc/lobotomized-claude-code
  ln -s ~/.tweakcc/lobotomized-claude-code/system-prompts-lcc ~/.tweakcc/system-prompts
  ln -s ~/.tweakcc/lobotomized-claude-code/system-reminders ~/.tweakcc/system-reminders
  pnpm dlx tweakcc-fixed@latest --apply
)
```

If either path already contains your overrides, merge the files you want to keep before replacing it with a symlink. The setup above stops instead of deleting existing directories.

The measured build used tweakcc main after `13b46f57`; npm v2.9.23 predates its empty-scaffold cleanup. See [tweakcc's source-build instructions](https://github.com/skrabe/tweakcc-fixed#build-from-source) to reproduce that build.

Restart Claude Code into a fresh session after applying. Run `--apply` again after Claude Code updates; `--restore` restores the original binary.

## Files

| Path                                           | Purpose                                                                  |
| ---------------------------------------------- | ------------------------------------------------------------------------ |
| [`system-prompts-lcc/`](system-prompts-lcc/)   | Named prompt fragments, tool descriptions, references and bundled skills |
| [`system-reminders/`](system-reminders/)       | Dynamic reminders injected during a session                              |
| [`docs/measurements.md`](docs/measurements.md) | Request-size fixture and catalogue counts                                |
| [`CLAUDE.md`](CLAUDE.md)                       | Editing rules and variable checks                                        |

One shared folder serves both models. Claude Code selects their model-specific fragments. Native routing is the default: `settings.misc.autonomousOperationAllModels` is `false`.

## Editing

Each Markdown file has an HTML-comment header followed by its replacement text. An empty body suppresses that fragment. Keep `ccVersion` and `${VAR}` bindings valid for the installed version; [CLAUDE.md](CLAUDE.md) explains the checks.

Validate before applying your edits:

```sh
pnpm dlx tweakcc-fixed@latest --validate-system-prompts
pnpm dlx tweakcc-fixed@latest --apply
```

## License

Derivative overrides of Claude Code's prompts, © Anthropic. Unaffiliated with Anthropic. MIT.
