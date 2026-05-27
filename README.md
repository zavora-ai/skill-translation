# Translation Skill

> Multilingual translation for AI agents — 200+ languages, language detection, batch translation, and human-verified translation memory. Zero config, free, no API keys.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--translate-green)](https://github.com/zavora-ai/mcp-translate)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Calls | What It Achieves |
|----------|-------|------------------|
| Translate | 1-2 | Detect source → translate with quality score |
| Batch | 1 | Translate to multiple languages at once |
| Verify | 1 | Find human-verified translations |
| Detect | 1 | Identify unknown language |

### Key Features
- **200+ languages** — including African languages (Swahili, Amharic, Yoruba)
- **Zero configuration** — no API keys needed
- **Quality scoring** — confidence score on every translation
- **Translation memory** — human-verified translations available
- **Batch support** — multiple targets in one call

## Installation

```bash
git clone https://github.com/zavora-ai/skill-translation.git \
  ~/.skills/skills/translation
```

## Requirements

**Required:** `mcp-translate` (5 tools — MyMemory, free, no API keys)

**Cross-MCP:**
- `mcp-email` — send responses in customer's language
- `mcp-cms` — localize content for multiple markets
- `mcp-customer-service` — bridge language gaps in support

## Folder Structure

```
translation/
├── SKILL.md                       # Decision tree + workflows + quality rules
├── scripts/
│   └── quality_check.py           # Flag low-confidence translations
├── references/
│   ├── tool-sequences.md          # 5 tools + language codes
│   ├── cross-mcp-workflows.md     # Translation + Email + CMS + CS
│   └── examples.md                # Translate, detect, batch (African examples)
├── README.md
└── LICENSE
```

## Example

**User:** "What language is this customer writing in? 'Ninahitaji msaada'"

**Result:**
```
Language: Swahili (97% confidence)
Translation: "I need help"
Recommendation: Respond in Swahili for best customer experience
```

## Success Criteria

| Metric | Target |
|--------|--------|
| Quality | Confidence score on every translation |
| Detection | Correct language ID before translating |
| Critical content | Flag for human review if score < 70% |

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0

---

Part of the [ADK-Rust Enterprise](https://enterprise.adk-rust.com) skills ecosystem. Built with ❤️ by [Zavora AI](https://zavora.ai)
