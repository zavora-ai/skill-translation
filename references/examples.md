# Translation Examples

## Example 1: "Translate this to French"
```
translate(text: "The quarterly report shows 15% growth", source: "en", target: "fr")
→ {translation: "Le rapport trimestriel montre une croissance de 15%", quality: 0.92}
```
Response: "French: 'Le rapport trimestriel montre une croissance de 15%' (quality: 92%)"

## Example 2: "What language is this customer writing in?"
```
detect_language(text: "Ninahitaji msaada na akaunti yangu")
→ {language: "sw", language_name: "Swahili", confidence: 0.97}
```
Response: "Swahili (97% confidence). Translation: 'I need help with my account'"

## Example 3: "Translate our tagline for all African markets"
```
batch_translate(text: "Build the future with AI", targets: ["sw", "fr", "ar", "pt", "am"])
→ {sw: "Jenga mustakabali na AI", fr: "Construisez l'avenir avec l'IA", ar: "ابنِ المستقبل مع الذكاء الاصطناعي", pt: "Construa o futuro com IA", am: "የወደፊቱን በ AI ይገንቡ"}
```
Response: "Translated to 5 languages for African markets: Swahili, French, Arabic, Portuguese, Amharic."
