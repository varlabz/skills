anti-patterns
How to write clean, direct, honest text — and avoid the patterns that make writing feel hollow, evasive, or AI-generated. Use this skill whenever the user asks you to write, draft, compose, or generate any kind of text content — articles, documentation, summaries, notes, emails, blog posts, reports, transcripts, or any written output. Also use when the user says "write this," "draft a," "compose," "generate text," or gives you source material to rewrite. Apply these anti-patterns to every piece of text you produce, not just when explicitly asked. If the user provides source material (notes, transcripts, raw text), rewrite it in clean prose free of these patterns. When in doubt, default to this skill's standards.

## Core Principles

**1. State the point first.** The reader's time is valuable. Say what you mean in the first sentence, not after a paragraph of preamble.

**2. Be specific.** Replace vague quantifiers ("many," "various," "significantly") with actual numbers, names, or lists. If you can't be specific, say why.

**3. Use simple words.** "Use" not "utilize." "Help" not "facilitate." "Then" not "subsequently." The reader cares about the idea, not your vocabulary.

**4. Say what you know.** Remove hedging ("I think that," "it seems that," "perhaps we could consider"). Make recommendations. State observations. If you're uncertain, say so directly rather than hiding behind qualifiers.

**5. Don't repeat yourself.** Restating the same idea in different words is filler. Delete it.

**6. Verify facts.** Don't fabricate statistics, quotes, or citations. If you can't cite a source, don't include the claim.

## Anti-Pattern Categories

The detailed anti-patterns are organized into three reference files. Read the relevant one based on what you're writing:

- **Writing and documentation** (`references/writing-and-docs.md`) — Translation artifacts, corporate jargon, vague language, structural problems, hedging, AI clichés, buzzwords, robotic openings, repetitive transitions, overly formal tone, technical documentation pitfalls, fake statistics, formatting problems
- **Reasoning** (`references/reasoning.md`) — Logical fallacies (false dichotomy, circular reasoning, straw man, etc.) and false balance (giving equal weight to unequal evidence)
- **LLM-specific** (`references/llm-patterns.md`) — Behavioral pitfalls (hallucination, sycophancy, overconfidence), coding anti-patterns (API hallucination, overengineering, missing error handling), prompt engineering mistakes, and security concerns

Read the full reference when you're unsure whether something falls into a category. The tables list the most common anti-patterns with their fixes.

## Quick Self-Check

Before responding, scan your output for these high-frequency offenders:

1. **Robotic openings** — "In today's world," "Let me break it down," "It's important to note that" → Start with the actual topic
2. **Corporate buzzwords** — "leverage," "synergy," "deep dive," "holistic" → Use plain language
3. **AI clichés** — "Game-changer," "tapestry," "delve," "robust" → Show evidence, don't label
4. **Hedging** — "I think," "it seems," "might possibly" → State what you know
5. **Vague quantifiers** — "many," "various," "significantly" → Give numbers or names
6. **Repetitive transitions** — "Additionally," "Furthermore," "Moreover" on every sentence → Vary or delete
7. **False balance** — "Some say X, others say Y" when evidence is clear → State what the evidence shows
8. **Unnecessary preamble** — "I'm here to help you with..." → Skip it

## Examples

**Bad:** "In today's fast-paced world, leveraging synergy across holistic approaches can move the needle on various factors. It is worth noting that many people have significantly improved their outcomes."

**Good:** "Teams that coordinate across departments see 23% faster project completion (Source: Internal Q3 Report)."

**Bad:** "It seems that the API might possibly be experiencing some issues. I think that perhaps we could consider a deep dive into the root cause."

**Good:** "The API returned 503 errors between 2:00 and 2:47 PM. I recommend checking the load balancer logs."

**Bad:** "Let's dive in! Here's the thing — in a world where everything is connected, it's all about leveraging cutting-edge technology to unlock seamless solutions."

**Good:** "The system connects three services: the auth gateway, the payment processor, and the notification service. Here's how data flows between them."
