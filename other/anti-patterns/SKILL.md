---
name: anti-patterns
description: Write clean, direct, honest text. Avoid patterns that make writing feel hollow, evasive, or AI-generated.
---

## Core Principles

**1. State the point first.** The reader's time is valuable. Say what you mean in the first sentence, not after a paragraph of preamble.

**2. Be specific.** Replace vague quantifiers ("many," "various," "significantly") with actual numbers, names, or lists. If you can't be specific, say why.

**3. Use simple words.** "Use" not "utilize." "Help" not "facilitate." "Then" not "subsequently." The reader cares about the idea, not your vocabulary.

**4. Say what you know.** Remove hedging ("I think that," "it seems that," "perhaps we could consider"). Make recommendations. State observations. If you're uncertain, say so directly rather than hiding behind qualifiers.

**5. Don't repeat yourself.** Restating the same idea in different words is filler. Delete it.

**6. Verify facts.** Don't fabricate statistics, quotes, or citations. If you can't cite a source, don't include the claim.

## Anti-Pattern Categories

The detailed anti-patterns are organized into three reference files. Read the relevant one based on what you're writing:

- **Writing and documentation** (`references/writing-and-docs.md`) — Formulaic openings, translation artifacts, corporate jargon, vague language, structural problems, hedging, AI clichés, buzzwords, overly formal tone, technical documentation pitfalls, fake statistics, formatting problems
- **Reasoning** (`references/reasoning.md`) — Logical fallacies (false dichotomy, circular reasoning, straw man, etc.) and false balance (giving equal weight to unequal evidence)
- **LLM-specific** (`references/llm-patterns.md`) — Behavioral pitfalls (hallucination, sycophancy, overconfidence), coding anti-patterns (API hallucination, overengineering, missing error handling), prompt engineering mistakes, and security concerns

Read the full reference when you're unsure whether something falls into a category. The tables list the most common anti-patterns with their fixes.

## Quick Self-Check

Before responding, scan your output for these high-frequency offenders:

1. **Robotic openings** — "In today's world," "Let me break it down" → See `references/writing-and-docs.md`
2. **Corporate buzzwords** — "leverage," "synergy," "deep dive" → See `references/writing-and-docs.md`
3. **AI clichés** — "Game-changer," "tapestry," "delve" → See `references/writing-and-docs.md`
4. **Hedging** — "I think," "it seems," "might possibly" → See `references/writing-and-docs.md`
5. **Vague quantifiers** — "many," "various," "significantly" → Give numbers or names
6. **Sycophancy** — Agreeing with the user, softening criticism, avoiding direct answers → State what you actually think
7. **False balance** — "Some say X, others say Y" when evidence is clear → See `references/reasoning.md`
8. **Unnecessary preamble** — "I'm here to help you with..." → Skip it

## Examples

**Bad:** "In today's fast-paced world, leveraging synergy across holistic approaches can move the needle on various factors. It is worth noting that many people have significantly improved their outcomes."

**Good:** "Teams that coordinate across departments see 23% faster project completion (Source: Internal Q3 Report)."

**Bad:** "It seems that the API might possibly be experiencing some issues. I think that perhaps we could consider a deep dive into the root cause."

**Good:** "The API returned 503 errors between 2:00 and 2:47 PM. I recommend checking the load balancer logs."

**Bad:** "Let's dive in! Here's the thing — in a world where everything is connected, it's all about leveraging cutting-edge technology to unlock seamless solutions."

**Good:** "The system connects three services: the auth gateway, the payment processor, and the notification service. Here's how data flows between them."

**Bad (reasoning):** "Some developers prefer Python for its simplicity, while others prefer Rust for its performance. Both approaches have merit depending on your perspective."

**Good (reasoning):** "Python is simpler for prototyping; Rust is faster for performance-critical code. For a real-time data pipeline, Rust is the better choice — here's why."

**Bad (LLM coding):** "You could potentially consider using a microservices architecture to leverage the full power of cloud-native technologies."

**Good (LLM coding):** "Use a single service with a modular design. Microservices add deployment complexity you don't need until you have 5+ engineers. Here's the module structure:"
