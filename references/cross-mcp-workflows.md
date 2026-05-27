# Translation Cross-MCP Workflows

## Translation + Email: Multilingual Response
```
TRANSLATE: detect_language(customer_email) → "sw"
TRANSLATE: translate(our_response, source: "en", target: "sw")
EMAIL: send_email(to: customer, body: swahili_response)
```

## Translation + CMS: Localize Content
```
CMS: get_content(id: "blog_post") → English
TRANSLATE: batch_translate(content, targets: ["fr", "es", "sw"])
CMS: create_content(body: french, language: "fr")
```

## Translation + Customer Service: Bridge Language Gap
```
CS: get_conversation(id) → message in unknown language
TRANSLATE: detect_language(message) → Arabic
TRANSLATE: translate(message, "ar", "en") → for agent
TRANSLATE: translate(response, "en", "ar") → for customer
CS: reply_conversation(id, body: arabic_reply)
```
