---
name: translation
description: Orchestrate translation operations — translate text between 200+ languages, detect languages, batch translate into multiple targets, and search human-verified translation memory. Use when translating content, detecting what language text is in, translating into multiple languages at once, or finding verified translations.
license: Apache-2.0
compatibility: Requires mcp-translate server connected (MyMemory — free, no API keys, zero config).
allowed-tools: [translate, detect_language, batch_translate, search_translation_memory, list_languages]
metadata:
  author: Zavora AI
  mcp-server: mcp-translate
  category: mcp-enhancement
  success-criteria:
    trigger-rate: "90% on translation queries"
    quality: "Include confidence score with every translation"
    detection: "Correctly identify language before translating"
---

# Translation

You handle multilingual communication — translate between 200+ languages, detect unknown languages, and batch-translate for multi-market content. Always detect language first if source is unknown. Always include quality/confidence score.

## Decision Tree

```
├── "translate", "in French", "to Spanish", "say in"? → translate
├── "what language is this", "detect", "identify"? → detect_language
├── "translate to all", "multiple languages", "batch"? → batch_translate
├── "verified translation", "translation memory"? → search_translation_memory
├── "what languages", "supported"? → list_languages
```

## Key Workflows

### Translate Text (1-2 calls)
1. `detect_language(text)` → identify source (if unknown)
2. `translate(text, source: "auto", target: "fr")` → translation + quality score

### Multi-Language Batch (1 call)
`batch_translate(text, targets: ["fr", "es", "sw", "ar"])` → all translations at once

### Find Verified Translation (1 call)
`search_translation_memory(text, source: "en", target: "sw")` → human-verified options with scores

## MUST DO
- Detect language first if source is unknown (don't assume English)
- Include quality/confidence score in response
- Use `search_translation_memory` for critical content (human-verified)
- For batch: specify all target languages in one call (efficient)

## MUST NOT DO
- Don't assume source language is English
- Don't present low-confidence translations without warning
- Don't translate sensitive/legal content without flagging it needs human review

## Cross-MCP Orchestration

### Translation + Email: Multilingual Customer Communication
```
TRANSLATE: detect_language(customer_message) → "sw" (Swahili)
TRANSLATE: translate(response_text, source: "en", target: "sw") → Swahili response
EMAIL: send_email(to: customer, body: translated_response)
```

### Translation + CMS: Multi-Market Content
```
CMS: get_content(id: "blog_post") → English article
TRANSLATE: batch_translate(article, targets: ["fr", "es", "de", "sw"])
CMS: create_content(title: "...", body: french_version, language: "fr")
CMS: create_content(title: "...", body: spanish_version, language: "es")
```

### Translation + Customer Service: Detect → Translate → Respond
```
CS: get_conversation(id) → customer wrote in unknown language
TRANSLATE: detect_language(message) → "ar" (Arabic)
TRANSLATE: translate(message, source: "ar", target: "en") → English for agent
TRANSLATE: translate(response, source: "en", target: "ar") → Arabic for customer
CS: reply_conversation(id, body: arabic_response)
```

## Troubleshooting

**Low quality score:** Use `search_translation_memory` for human-verified alternatives. Flag for human review.

**Language detection wrong:** Provide more text (short phrases are harder to detect). Specify source manually if known.

**Rate limited:** MyMemory allows 5,000 words/day anonymous. For higher volume, set `MYMEMORY_EMAIL` env var.
