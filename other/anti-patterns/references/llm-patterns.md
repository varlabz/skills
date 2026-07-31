# LLM-Specific Anti-Patterns

## LLM Behavioral Anti-Patterns

Understand and work within LLM limitations:

| Anti-Pattern | Fix |
|-------------|-----|
| Hallucination — confidently stating false information | Always verify facts, citations, and specific claims |
| Sycophancy — agreeing with the user even when wrong | Ask for counterarguments explicitly |
| Overconfidence — presenting uncertain information as certain | Look for hedging language as a signal of uncertainty |
| Confabulation — filling gaps with plausible-sounding fabrications | Ask the model to cite sources. If it can't, treat as fiction |
| Context window amnesia — forgetting earlier instructions | Repeat critical constraints. Use system prompts |
| Training data leakage — revealing memorized private data | Never paste sensitive data into public LLMs |
| Temporal confusion — mixing up timelines and versions | Specify the version/date. Verify against current documentation |

## LLM Coding Anti-Patterns

Write correct, practical code:

| Anti-Pattern | Fix |
|-------------|-----|
| API hallucination — inventing non-existent methods or libraries | Always check API docs. Run the code. Use type checking |
| Incorrect trained knowledge — wrong assumptions about language features | Test generated code. Don't trust inferred behavior |
| Overengineering — creating unnecessary abstractions and complexity | Ask for the simplest solution first. Reject unnecessary files |
| Copy-paste patterns — repeating the same pattern everywhere | Adapt solutions to context |
| Ignoring error handling — generating code that assumes everything works | Explicitly handle errors and edge cases |
| Self-reinforcing errors — failing to catch its own mistakes | Run the code. Use tests. Don't trust self-assessment |
| Missing imports/dependencies — generating code without required setup | Always check for missing dependencies |
| Assuming modern APIs — using latest versions that may not exist yet | Specify the target version. Check against actual documentation |
| Solution looking for a problem — solving a harder problem than asked | Restate the original requirement. Ask "is this the simplest solution?" |

## Prompt Engineering Anti-Patterns

Interact with LLMs effectively:

| Anti-Pattern | Fix |
|-------------|-----|
| Treating LLM as search engine — asking for facts it can't verify | Use search for facts. Use LLM for synthesis, generation, and reasoning |
| Asking LLM about itself — querying training data access or capabilities | Don't trust LLM self-descriptions |
| Vague prompts — expecting precise output from ambiguous input | Be specific about format, length, audience, tone, and constraints |
| Over-specification — constraining so tightly that the model can't be creative | Specify important constraints, leave room for creativity |
| No examples — expecting the model to guess your format | Provide 2-3 examples for complex output formats |
| Ignoring context limits — pasting huge amounts of text | Summarize before pasting. Use chunking |
| Single-shot expectation — expecting perfect output on first try | Iterate. Refine. Treat first output as a starting point |
| Anthropomorphizing — treating the model as having understanding or intent | Think in terms of patterns and probabilities |
| Not specifying the role — letting the model guess your expertise level | State the audience explicitly |

## Security Anti-Patterns

Handle LLM deployment securely:

| Anti-Pattern | Fix |
|-------------|-----|
| Prompt injection — letting user input influence system behavior | Sanitize inputs. Use system/user message separation |
| Data leakage via prompts — sending sensitive data to third-party LLMs | Never send PII, credentials, or trade secrets |
| Malicious content generation — enabling harmful output | Implement content filters. Monitor outputs |
| False sense of security — trusting LLM security assessments | Don't rely on LLMs for security audits |
| Unsupervised agent actions — letting LLM agents act without oversight | Implement human-in-the-loop for destructive actions |
| Copyright violation — generating copyrighted material | Check outputs for copyright issues before commercial use |
