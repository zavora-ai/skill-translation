# Translation Tool Sequences (5 tools)

| Tool | Purpose | Input | Output |
|------|---------|-------|--------|
| `translate` | Translate text | text, source, target | translation, quality_score |
| `detect_language` | Identify language | text | language_code, confidence |
| `batch_translate` | Multi-target | text, targets[] | {lang: translation}[] |
| `search_translation_memory` | Human-verified | text, source, target | matches with scores |
| `list_languages` | Supported langs | — | 200+ language codes |

## Language Codes (common)
en (English), fr (French), es (Spanish), de (German), pt (Portuguese), ar (Arabic), zh (Chinese), ja (Japanese), ko (Korean), sw (Swahili), hi (Hindi), ru (Russian)

## Sequence: Translate Unknown Language (2 calls)
```
1. detect_language(text: "Habari yako?") → {language: "sw", confidence: 0.98}
2. translate(text: "Habari yako?", source: "sw", target: "en") → {translation: "How are you?", quality: 0.95}
```

## Sequence: Multi-Market Content (1 call)
```
batch_translate(text: "Welcome to our platform", targets: ["fr", "es", "sw", "ar"])
→ {fr: "Bienvenue sur notre plateforme", es: "Bienvenido a nuestra plataforma", sw: "Karibu kwenye jukwaa letu", ar: "مرحبا بكم في منصتنا"}
```
