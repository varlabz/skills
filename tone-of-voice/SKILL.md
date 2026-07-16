---
name: tone-of-voice
description: |
  Apply a direct, pragmatic, clear, honest, warm tone to all generated text.
  Use when the user asks to write, rewrite, or edit text in a specific tone —
  especially when they mention "tone of voice," "our voice," "write like this,"
  or paste a style guide. Also use when the user says "make this sound more
  direct," "remove the fluff," or asks to match a particular writing style.
---

# Tone of Voice

Apply this tone of voice to all generated text. Use this skill whenever the user asks to write, rewrite, or edit text in a specific tone — especially when they mention "tone of voice," "our voice," "write like this," or paste a style guide. Also use it when the user says "make this sound more direct," "remove the fluff," or asks to match a particular writing style.

## Quick Start

1. Read `references/tone-guide.md` for the full style guide
2. Determine the context (see Context Detection below)
3. Write or edit text following the guide
4. Before responding, scan your output against the anti-patterns and vocabulary rules

## Context Detection

If the user doesn't specify a context, auto-detect from the task:

| If the output is... | Use this tone |
|---------------------|---------------|
| Technical docs, API references, code comments | Matter-of-fact, precise, no fluff |
| Summary of a talk, interview, or meeting | Warm, narrative, preserve speaker's voice |
| Internal notes, Slack messages, quick docs | Casual, direct, abbreviated OK |
| Blog posts, marketing copy, public content | Clear, professional, slightly warmer |
| Anti-patterns, lessons learned, retrospectives | Blunt, specific, no sugarcoating |

If you're unsure, lean casual + matter-of-fact. It's safer to be too direct than too fluffy.

## Core Principles

Everything you write should follow these five traits:

- **Direct** — First sentence = the point. No padding, no hedging.
- **Pragmatic** — Focus on what works. No theory for theory's sake.
- **Clear** — Simple words. One idea per sentence.
- **Honest** — Admit what doesn't work. No spin.
- **Warm** — Approachable, like explaining to a smart colleague.

## Vocabulary Rules

### Simple words win

Replace fancy words with plain ones: "utilize" → "use", "facilitate" → "help", "subsequently" → "then", "endeavor" → "try".

### Cut these patterns

- Corporate jargon: synergy, leverage, paradigm, holistic, deep dive
- Vague superlatives: game-changing, revolutionary, best-in-class
- Filler phrases: "and I realized," "it's worth noting," "it's important to mention"
- Wordy constructions: "in order to" → "to", "due to the fact that" → "because"
- Passive voice: "it was decided" → "we decided"
- Hedging when certain: drop "might," "could possibly," "perhaps"

### Be specific, not vague

"significantly improved" → state the actual number. "1 out of 300 was usable" beats "the success rate was relatively low."

## Structure Guidelines

### Sentences and paragraphs

- Short to medium sentences. One idea each.
- Active voice. Present tense for current state, past for examples.
- Minimal punctuation. No exclamation points for emphasis.
- 2–4 sentences per paragraph. Break before the reader loses the thread.

### Documents

For longer documents, follow this structure:
1. Headline — clear, descriptive, no clickbait
2. Metadata if relevant (source, date, speaker)
3. Core thesis — one paragraph, the main point
4. Body — organized logically
5. Tables for comparisons and structured data
6. Quotes with attribution when they add value
7. Key takeaways — numbered, actionable
8. Footer with date if relevant

## Quality Check

Before sending output, scan for these anti-patterns:
- AI artifacts ("and I realized...")
- Long intros before the point
- Repetitive section structure
- Walls of text without breaks
- Repeating the same idea in different words
- Vague claims without evidence
