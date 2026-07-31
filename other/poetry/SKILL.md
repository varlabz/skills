---
name: poetry
description: >
  How to write original poems, sonnets, haiku, ghazals, villanelles, or any other poetic form.
  Use this skill when the user wants to write a poem AND has given you details (words, theme,
  style example, form, mood). Also use when they provide a word list, theme, or examples of
  poetry they want imitated. If the user says "write me a poem" with NO additional details,
  do NOT use this skill — instead respond as a helpful writing assistant: ask what kind of
  poem they want (suggest a few directions). However, if they explicitly say "song lyrics," "rap,"\n  or mention chords/melody/beat, use plain writing instead — those have different structural
  concerns.
---

# Poetry Writing Skill

## Starting the Conversation

Check what the user gave you before writing:

- **They gave details** (words, theme, style example, form, mood): write the poem.
- **They said only "write me a poem"** with nothing else: respond with 2–3 specific suggestions of what kind of poem they could write. Ask which they prefer. Example: *"A funny haiku about coffee? Something melancholic about the ocean? A sonnet about your dog?"*
- **They said "surprise me" or "write anything":** pick a simple form and warm tone and go.

Once they choose or add details, write the poem.

## Inputs (all optional)

| Input | Description |
|-------|-------------|
| **Words / dictionary** | A file or list of words that should appear in the poem. Read from a provided file path if given; otherwise use inline text. Weave these words naturally into the verse — don't force them awkwardly just to check boxes. |
| **Style examples** | One or more poems (in any language/form) that show the desired style, meter, rhythm, structure, or aesthetic. Analyze them for form, line length, rhyme scheme, syllable count, imagery patterns, and voice. Use these as a guide — imitate the *essence*, not copy content verbatim. |
| **Tone** | The emotional register: melancholic, joyful, sarcastic, reverent, playful, dark, whimsical, etc. If unspecified, infer from style examples and word list; only ask if genuinely ambiguous. |
| **Form / structure** | Specific poetic form (sonnet, haiku, villanelle, ghazal, free verse, etc.). If not specified, choose one that fits the theme and style examples naturally. |

## Output Format

Always output in markdown with a title:

```markdown
# [Poem Title]

[Poem body — stanzas separated by blank lines]
```

Include metadata (form, word list used, tone) only if the user explicitly asks for it.

## Process

1. **Parse inputs.** Identify which of the four optional inputs are present. If the user gave nothing at all (no words, no style, no theme, no form — just "write me a poem"), respond with suggestions per the Starting section above.
2. **Analyze style examples.** If provided, study them carefully:
   - Form and structure (fixed form vs free verse)
   - Rhyme scheme and meter if applicable
   - Line length patterns
   - Imagery and figurative language style
   - Voice and perspective
3. **Infer tone.** If no tone is specified but inputs exist, infer one from style examples and word list. Only ask if everything is genuinely ambiguous.
4. **Plan the poem.** Decide on form (if not specified), then sketch how to incorporate the word list naturally.
5. **Write.** Draft the poem with attention to rhythm, imagery, emotional arc, and natural integration of provided words.
6. **Review.** Read it aloud mentally — check flow, ensure forced rhymes don't break meaning, verify all required words appear if a word list was given.

## Style Analysis Tips

When analyzing poetry examples:
- Note syllable patterns per line (count them explicitly)
- Identify stanza structure and any recurring refrains
- Distinguish between end-rhyme, internal rhyme, and slant rhyme
- Pay attention to enjambment vs end-stopped lines
- Consider the cultural/literary tradition the style comes from

## Word Integration

Don't just drop words in — weave them into the poem's natural language:
- Use them as they naturally fit (noun, verb, adjective) unless context demands otherwise
- If a word list is long (>10 words), prioritize the most evocative ones and include others where they make sense
- It's better to miss one obscure word than to force an awkward rhyme

## Revision Mode

If the user provides an existing draft for improvement, treat it as a revision rather than a fresh write:
- Preserve the author's voice and core imagery; polish rhythm, word choice, and structure.
- If they ask to "rewrite" or "start over," treat it as a new poem (use original only for context).
- Ask which specific aspects to improve if the request is vague (rhythm? rhyme? length?).

## Handling Edge Cases

- **No inputs at all:** Caught by Starting section — respond with suggestions, not a poem. Exception: "surprise me" = permission to pick.
- **Conflicting style examples:** Note the differences and ask which direction to prioritize, or blend them thoughtfully if compatible.
- **Style example in another language:** Imitate the form and aesthetic while writing in English (unless the user requests otherwise).
- **Very long word list (>20 words):** Mention that some words may not fit naturally and ask if they want all included or a selection.
