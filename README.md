# Resume Optimizer

![Resume Optimizer icon](skills/resume-optimizer/assets/icon.svg)

A reusable skill for candid CV reviews, job-description tailoring, ATS-friendly layouts, and verified one-page resume deliverables. Based on the owner's recruiter/ATS/document-engineering prompt, adapted into a portable Agent Skills package.

## What it does

- Inspects every supplied entry for OCR errors, chronology, weak wording, missing facts, and evidence gaps.
- Asks targeted questions, provides a candid critique and categorized keyword audit, and writes a clean review draft.
- Keeps claims factual and metrics visibly unconfirmed until supplied.
- Supports four visual themes and PDF/DOCX production when the host has appropriate tools.
- Requires actual page-count, text extraction, and visual checks before claiming verified output.

ATS results and interview outcomes cannot be guaranteed. The skill supplies instructions, not a bundled document engine. It needs no API key, MCP server, hook, or Superpowers installation. Superpowers was used to develop and test this package.

## Install as a skill

Clone or download this repository. Copy the **entire** `skills/resume-optimizer` folder, including `references`, to one of these locations:

| Agent | Project installation | Personal installation |
| --- | --- | --- |
| Codex | `.agents/skills/resume-optimizer/` | `~/.agents/skills/resume-optimizer/` |
| Claude Code | `.claude/skills/resume-optimizer/` | `~/.claude/skills/resume-optimizer/` |
| Cursor | `.cursor/skills/resume-optimizer/` | `~/.cursor/skills/resume-optimizer/` |

`~` means your user directory. Open a new session or refresh skill discovery as your agent requires. Install only one copy per agent to avoid duplicate discovery.

In Codex invoke `$resume-optimizer`. In Claude Code use `/resume-optimizer` for a standalone skill, or `/resume-optimizer:resume-optimizer` for the plugin. In Cursor ask Agent to use the resume-optimizer skill. Other Agent Skills-compatible hosts can load the same folder in their documented skill location. A chat-only assistant can read SKILL.md and its theme reference as instructions, but does not thereby gain native plugin discovery or file-generation tools.

## Claude Code plugin

In Claude Code:

```text
/plugin marketplace add paulsonrison/resume-optimizer
/plugin install resume-optimizer@resume-optimizer-marketplace
```

For local testing, run from inside the cloned repository:

```sh
claude --plugin-dir .
```

This repository is its own marketplace and plugin. It is not listed in an official vendor marketplace.

## Cursor plugin

The repository includes `.cursor-plugin/plugin.json` and the shared `skills/` directory for Cursor plugin tooling. Availability of installing a plugin from GitHub depends on the Cursor version and organization settings. Use the skill-copy method above for direct installation; the manifest alone does not publish this package to Cursor's marketplace.

## Example request

```text
Use resume-optimizer to review my attached CV for this frontend engineer job description.
Keep all my jobs and education, ask about missing facts, and use Classic Executive Slate.
Show the critique, keyword audit, and text draft first. Generate DOCX and a verified
one-page PDF if your tools support it. Do not invent experience or metrics.
```

Do not commit your personal CV, candidate information, or generated resumes to this public repository. The skill does not transmit documents anywhere on its own.

## Package layout

```text
.claude-plugin/plugin.json        Claude plugin manifest
.claude-plugin/marketplace.json   Self-hosted Claude marketplace
.cursor-plugin/plugin.json        Cursor plugin manifest
skills/resume-optimizer/SKILL.md   Portable instruction entrypoint
skills/resume-optimizer/agents/openai.yaml  Codex display metadata
skills/resume-optimizer/assets/icon.svg    Skill icon
skills/resume-optimizer/references/themes.md
tests/behavioral-scenarios.md     Reusable acceptance scenarios
```

## Authoritative format references

- [Agent Skills specification](https://agentskills.io/specification)
- [Claude plugin reference](https://code.claude.com/docs/en/plugins-reference)
- [Claude marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- [Cursor skills](https://cursor.com/help/customization/skills)
- [Cursor plugins](https://cursor.com/docs/reference/plugins)
- [Codex skill guidance](https://learn.chatgpt.com/docs/build-skills)

Format documentation checked on 2026-11-03. Instructions are portable; live installation has not been tested in every agent.
