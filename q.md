## 21 Chunking Strategies for RAG. And how to choose the right one for… …

![](https://ddlihl75qpk8y0.archive.is/1nxMc/9b9410c048ca0db961f29d86e9bcdbe348713e16/scr.png)archived 22 Jul 2025 11:13:01 UTC

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| [archive.today  webpage capture](https://archive.today/) | Saved from | |  |  | | --- | --- | | [![](data:image/svg+xml;base64...)history](https://archive.is/https%3A//ai.gopubby.com/21-chunking-strategies-for-rag-f28e4382d399 "3 snapshots from https://ai.gopubby.com/21-chunking-strategies-for-rag-f28e4382d399")[←prior](https://archive.is/Vpchk "20 Jul 2025 08:01:20 UTC") next→ |  | | 22 Jul 2025 11:13:01 UTC |
| All snapshots | **from host** [ai.gopubby.com](https://archive.is/ai.gopubby.com) | |
| [Webpage](https://archive.is/1nxMc)[Screenshot](https://archive.is/1nxMc/image) | |
| [![](data:image/svg+xml;base64...)share](https://archive.is/1nxMc/share)[![](data:image/svg+xml;base64...)download .zip](https://archive.is/download/1nxMc.zip)[![](data:image/svg+xml;base64...)report bug or abuse](https://archive.is/1nxMc/abuse)[![](data:image/svg+xml;base64...)Buy me a coffee](https://liberapay.com/archiveis/donate) | |

[![](data:image/svg+xml;base64...)](https://archive.is/1nxMc)

Reddit

VKontakte

Twitter

Pinboard

Livejournal

short link

long link

markdown

html code

<a href="http://archive.today/1nxMc">
<img style="width:300px;height:200px;background-color:white" src="/1nxMc/9b9410c048ca0db961f29d86e9bcdbe348713e16/scr.png"><br>
21 Chunking Strategies for RAG. And how to choose the right one for… …<br>
archived 22 Jul 2025 11:13:01 UTC
</a>

wiki code

{{cite web
| title = 21 Chunking Strategies for RAG. And how to choose the right one for… …
| url = https://ai.gopubby.com/21-chunking-strategies-for-rag-f28e4382d399
| date = 2025-07-22
| archiveurl = http://archive.today/1nxMc
| archivedate = 2025-07-22 }}

[Sitemap](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/sitemap/sitemap.xml)

[Open in app](https://archive.is/o/1nxMc/https%3A//rsci.app.link/?$canonical_url=https://medium.com/p/f28e4382d399&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[Sign up](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/21-chunking-strategies-for-rag-f28e4382d399)

[Sign in](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/21-chunking-strategies-for-rag-f28e4382d399)

[Medium Logo](https://archive.is/o/1nxMc/https%3A//medium.com/)

[Write](https://archive.is/o/1nxMc/https%3A//medium.com/new-story)

[Sign up](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/21-chunking-strategies-for-rag-f28e4382d399)

[Sign in](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/21-chunking-strategies-for-rag-f28e4382d399)

![](https://ddlihl75qpk8y0.archive.is/1nxMc/159539ec813ac5dc13ca6ec7f110f1224359a170.png)

[## AI Advances](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/)

·

[Follow publication](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/21-chunking-strategies-for-rag-f28e4382d399)

[![AI Advances](data:image/gif;base64...)](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/)

Democratizing access to artificial intelligence

[Follow publication](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/21-chunking-strategies-for-rag-f28e4382d399)

Top highlight

Member-only story

# 21 Chunking Strategies for RAG

## And how to choose the right one for your next LLM application

[![Anjolaoluwa Ajayi](https://ddlihl75qpk8y0.archive.is/1nxMc/0006239efca44b235152f7407945cf33814a616a.jpg)](https://archive.is/o/1nxMc/https%3A//medium.com/%40dataprincess)

[Anjolaoluwa Ajayi](https://archive.is/o/1nxMc/https%3A//medium.com/%40dataprincess)

Follow

8 min read

·

Jun 30, 2025

708

5

[Listen](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/21-chunking-strategies-for-rag-f28e4382d399)

Share

![](https://ddlihl75qpk8y0.archive.is/1nxMc/825986da957751f1600ec63497e5503f99fbeb6e.webp)

A Quick Refresher on RAG | Image by Author

Retrieval-Augmented Generation (RAG) is one AI technique many AI engineers hate to love (me included).

Yes, because, on [paper](https://archive.is/o/1nxMc/https%3A//arxiv.org/pdf/2005.11401), it sounds so simple: “*Retrieve* the right context from your custom data and let an LLM *generate* a response based on it.”

But in practice, you’re stuck wrangling gigabytes of messy data stored in the most chaotically random formats you’ve ever seen, then doing days of trial and error:

* tweaking chunks
* switching embedding models
* swapping out retrievers
* fine-tuning rankers
* rewriting prompts

And the model still says, “I don’t have enough info to answer your query.”

Or worse, it *confidently* churns out total nonsense (hallucinates).

No doubt, there are many moving parts in RAG, but one piece that quietly determines whether the whole thing works or not is **chunking**.

Different data types, file formats, content structures, document lengths, and use cases all call for different chunking strategies.

Get it wrong, and your model either misses the point or, well, misses the point…

In this article, we will look at 21 chunking strategies (from easy to advanced) and when to use each one so that your RAG systems stop… missing the point.

![](https://ddlihl75qpk8y0.archive.is/1nxMc/76f2069b2439574b931e39c0a58836abf42d3787.gif)

[Let’s Do This GIF](https://archive.is/o/1nxMc/https%3A//community.atlassian.com/forums/Welcome-Center-articles/Welcome-Wednesday-Get-excited-Team-25-is-next-week/ba-p/2969616)

# 1. Naive chunking (split by newline)

You split the text at every line break. That’s it.

![](https://ddlihl75qpk8y0.archive.is/1nxMc/4fa55afb6324e5cafe2d2cadc52885aac73a6d4a.webp)

Example of Naive chunking | Image by author

**When to use it:**

* For text that’s *uniformly* separated by newlines: notes, bullet lists, FAQs, chat logs, or transcripts where each line holds a complete thought.

**P.S.** If lines are too long, you could blow the LLM token limit. If they’re too short, the model might miss context or hallucinate.

# 2. Fixed-size/ fixed window chunking

You break the text into equal parts by word or character count (even if it cuts through a sentence or thought).

![](https://ddlihl75qpk8y0.archive.is/1nxMc/495dabd43f6f23cd1a7801f6d8dab5ab113208ed.webp)

Example of fixed-size chunking | Image by author

**When to use it:**

* For raw, messy text dumps, such as scanned documents, bad transcripts, or large text files with no punctuation or headings or… structure.

# **3. Sliding window chunking**

Like fixed-size chunking, but each chunk overlaps with the one before it to maintain context across chunks.

![](https://ddlihl75qpk8y0.archive.is/1nxMc/4877509ffab43c2eaef8ace2060277fa8ddc19f2.webp)

Example of sliding window chunking (Compare with fixed window chunking) | Image by author

**When to use it:**

* For content where ideas carry across long sentences, i.e. essays, narrative reports, free-form writings
* Just like fixed window chunking, it works for text with no structure (no heading, punctuation, schema, etc). Just be mindful of the tradeoff between token usage and broken context.

# 4. Sentence-based chunking

You break the text at the end of each sentence, usually marked by a full stop, question mark, or exclamation mark.

![](https://ddlihl75qpk8y0.archive.is/1nxMc/9b7510b2ceea467587e1af81431a890d4dfad18c.webp)

Example of sentence-based chunking | Image by author

**When to use it:**

* For clean, well-written text where each sentence holds a whole idea, like blogs, summaries, or documentation.
* As an initial step, to get small, focused chunks that can easily be reranked or recombined later using more complex chunking techniques.

# 5. Paragraph-based chunking

You split the text by paragraph (usually where there’s a double line break) so each chunk holds a full idea or thought block.

![](https://ddlihl75qpk8y0.archive.is/1nxMc/7f89c2e0a35d84e27c2d20bd38924e8d06663df2.webp)

Example of paragraph-based chunking | Image by author

**When to use it:**

* When sentence chunking feels too narrow, and you want more context per chunk.
* For documents that are already well-structured into paragraphs, like essays, blog posts, or reports

# 6. Page-based chunking

You treat each page as one chunk.

![](https://ddlihl75qpk8y0.archive.is/1nxMc/b60d25e45da046ccdbbd5aadc02974da70028470.webp)

Example of page-based chunking | Image by author

**When to use it:**

* When you’re working with paginated documents like scanned PDFs, slide decks, or books
* For workflows that rely on page layout i.e. need to reference page numbers in retrieval.

# 7. Structured chunking

You split the text based on a known structure like log entries, schema fields, HTML tags, or markdown elements.

![](https://ddlihl75qpk8y0.archive.is/1nxMc/0d70b11fc04888d2545f6e7b25acd9fcde4c082d.webp)

Example of structured chunking | Image by author

**When to use it:**

* If you’re working with structured or semi-structured data like logs, JSON records, CSV, or HTML docs.

# 8. Document-Based Chunking:

You chunk by using the natural structure of the document (headings, subheadings, and sections).

![](https://ddlihl75qpk8y0.archive.is/1nxMc/5544f4eae8ab3ff2e2ced27c8f3426bfd7677a54.webp)

Example of document-based chunking | Image by author

**When to use it:**

* When your source has clear sections and headings, such as in articles, manuals, textbooks, or research papers
* As an initial step for more advanced chunking strategies, like hierarchical chunking.

# 9. Keyword-based chunking

You break the text wherever specific keyword(s) appear. You determine the keyword(s) beforehand and treat them as logical split points.

![](https://ddlihl75qpk8y0.archive.is/1nxMc/d335b80e61017eb8d8276bfccc4b533f3afc22f8.webp)

Example of keyword-based chunking (keyword is ‘Note’)| Image by author

**When to use it:**

* When heading-level splits aren’t available but keyword phrases (that you know of) consistently mark new topics

# 10. Entity-based chunking

You use a named entity recognition (NER) model to detect entities like people, places, or products, then group related text around each one into chunks.

![](https://ddlihl75qpk8y0.archive.is/1nxMc/323922ff536c0e04e18cab6a27ade96e92f157c3.webp)

Example of entity-based chunking (keyword is ‘Note’)| Image by author

**When to use it:**

* For documents where specific entities matter, like news articles, legal contracts, case studies, or movie scripts.

# 11. Token-based chunking

You split the text by token count using a tokeniser.

You typically want to combine this technique with maybe sentence chunking to avoid splitting sentences in a way that kills context.

**When to use it:**

* For unstructured documents with no headings or paragraphing.
* When working with LLMs that have low token limits (to avoid truncation in response or processing).

# 12. Topic-based chunking

You break the text when the topic changes by:

* First, splitting it into smaller parts (sentences or paragraphs).
* Then, grouping related parts into a single chunk using topic modelling or clustering.

![](https://ddlihl75qpk8y0.archive.is/1nxMc/7179ad4c18d70378a998a33c626ddd65bb1fd8a4.webp)

Example of topic-based chunking by Clustering | Image by author

**When to use it:**

* When your document covers multiple topics and you want each chunk to stay focused on one idea
* For text where the topic shifts gradually but isn’t marked by explicit headings or keywords.

# 13. Table-aware chunking

You identify and chunk tables separately in JSON or Markdown format. It can be row by row, column by column, or the entire table.

![](https://ddlihl75qpk8y0.archive.is/1nxMc/5915ad6f3f32638c075c44e25aaf75d89edd58e6.webp)

Example of table-aware chunking | Image by author

**When to use it:**

* For documents that contain tables

# 14. Content-aware chunking

You adjust how you chunk based on the type of content, like using appropriate rules for paragraphs, tables, lists, etc.

**When to use it:**

* For mixed-format documents (that contain different text structures)
* When you want chunks that respect the document’s format and meaning, so tables stay whole, paragraphs stay intact, etc.

# 15. Contextual chunking

Use an LLM to:

* Analyse your knowledge base in part or whole
* And then add short, relevant context to each chunk before embedding.

![](https://ddlihl75qpk8y0.archive.is/1nxMc/9fb4fa2f23c3011d12f6b2edb8e10c1348cb87b4.webp)

Example of contextual chunking | Image by author

**When to use it:**

* When your knowledge base, in part/ whole, fits within the LLM token limit.
* For complex documents, such as financial reports and contracts.

# 16. Semantic chunking

You group sentences or paragraphs that talk about the same thing, using embedding similarity to keep chunks topically focused.

**When to use it:**

* When simpler techniques like paragraph or fixed window chunking fail
* For long documents with mixed topics

# **17. Recursive chunking**

You begin by splitting the text at a large separator (e.g., paragraphs).

If any resulting chunk exceeds your preset chunk size limit, you recursively split those chunks further using smaller separators (e.g., sentences or words) until all chunks are within the desired size.

**When to use it:**

* For text with uneven or unpredictable sentence lengths, like interviews, speeches, or free-form writing

# 18. Embedding chunking

Usually, you chunk then embed, but here, you embed all the sentences first, then go through them in order, grouping each one with the next if their similarity is high, and splitting only when it drops below a set threshold.

**When to use it:**

* When your document has no structure (sentence, heading, sections, markers, etc.)
* When simpler techniques (e.g., sliding window chunking) don’t cut it.

# 19. Agentic / LLM-based chunking

You ask the LLM to decide how to chunk the text and give it full control to break things up however it sees fit.

**When to use it:**

* When your content is complex or unstructured and needs human-like judgment to find good chunk boundaries

**Note**: This method can be costly or resource-intensive><

# **20. Hierarchical chunking**

You break the text into chunks at multiple levels, such as sections, subsections, and paragraphs, so that users can retrieve info at different levels of detail.

![](https://ddlihl75qpk8y0.archive.is/1nxMc/a4ebc276af4daa8c88b6bbf1b57964b4db57f643.webp)

**When to use it:**

* For documents that have clear sections and headings, such as in articles, manuals, textbooks, or research papers.
* If you want users to explore both broad overviews and detailed info without losing context.

# **21. Modality-Aware Chunking**

You separate different types of content (text, images, tables) in their own ways.

![](https://ddlihl75qpk8y0.archive.is/1nxMc/dce74c5348855d123be0c484bbbcb20acd4455ee.webp)

Example of modality-aware chunking | Image by author

# BONUS: Hybrid chunking

You combine different methods, heuristics, embeddings, and/or LLMs to get more reliable chunks.

**When to use it:**

* When no single chunking method fits your data perfectly, so you mix approaches for better results

# CTA

I hope this helps you take your RAG project to the next level.

If you enjoyed this read, give it up to **50 claps** to show some love.

Putting this together took weeks of research, writing, experimentation, and surprisingly design.

If you appreciate my work, you can tip me by clicking on the button below :D

![](https://ddlihl75qpk8y0.archive.is/1nxMc/82305a6f724df8b8eb2573418ca89ae8cd341d02.webp)

Thank you for indulging. Bye for now.

[Retrieval Augmented Gen](https://archive.is/o/1nxMc/https%3A//medium.com/tag/retrieval-augmented-gen)

[Artificial Intelligence](https://archive.is/o/1nxMc/https%3A//medium.com/tag/artificial-intelligence)

[Llm](https://archive.is/o/1nxMc/https%3A//medium.com/tag/llm)

[AI](https://archive.is/o/1nxMc/https%3A//medium.com/tag/ai)

708

708

5

[![AI Advances](https://ddlihl75qpk8y0.archive.is/1nxMc/775b25c0269e21ee5bd0de51f1b8dac0e2287cf9.png)](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/)

[![AI Advances](data:image/gif;base64...)](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/)

Follow

[## Published in AI Advances](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/)

[43K followers](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/followers)

·[Last published 8 hours ago](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/from-zero-to-20-million-tokens-my-ai-journey-for-first-half-of-2025-3f9cfcc83405)

Democratizing access to artificial intelligence

Follow

[![Anjolaoluwa Ajayi](https://ddlihl75qpk8y0.archive.is/1nxMc/dfa524da6c9524139475c031e030cb24be315fd2.jpg)](https://archive.is/o/1nxMc/https%3A//medium.com/%40dataprincess)

[![Anjolaoluwa Ajayi](data:image/gif;base64...)](https://archive.is/o/1nxMc/https%3A//medium.com/%40dataprincess)

Follow

[## Written by Anjolaoluwa Ajayi](https://archive.is/o/1nxMc/https%3A//medium.com/%40dataprincess)

[2.3K followers](https://archive.is/o/1nxMc/https%3A//medium.com/%40dataprincess/followers)

·[79 following](https://archive.is/o/1nxMc/https%3A//medium.com/%40dataprincess/following)

Remote Data Scientist. I'm a big data fiend (no pun intended ><). I mostly write about Data Science, ML, and Gen AI. Might write a book soon ;)

Follow

## Responses (5)

![](data:image/png;base64...)

Write a response

[What are your thoughts?](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/21-chunking-strategies-for-rag-f28e4382d399)

Cancel

Respond

[![Ciphernutz](https://ddlihl75qpk8y0.archive.is/1nxMc/ad69337bed27bbd0fe0ea45aafd3df8d10ff0dd5.png)](https://archive.is/o/1nxMc/https%3A//medium.com/%40ciphernutz)

[Ciphernutz](https://archive.is/o/1nxMc/https%3A//medium.com/%40ciphernutz)

[4 days ago (edited)](https://archive.is/o/1nxMc/https%3A//medium.com/%40ciphernutz/super-helpful-roundup-of-chunking-strategies-saved-this-for-my-next-rag-experiment-456fb08a9fd8)

```
Super helpful roundup of chunking strategies! Saved this for next RAG experiment
```

3

Reply

[![The Data Jockey](https://ddlihl75qpk8y0.archive.is/1nxMc/4131066909aa6f9791601d5239a44f257b8b6ddd.png)](https://archive.is/o/1nxMc/https%3A//medium.com/%40datajockeystreams)

[The Data Jockey](https://archive.is/o/1nxMc/https%3A//medium.com/%40datajockeystreams)

[Jun 30 (edited)](https://archive.is/o/1nxMc/https%3A//medium.com/%40datajockeystreams/as-someone-who-is-working-on-building-genai-powered-data-governance-tools-i-often-struggle-with-ecebc15ea072)

```
As someone who is working on building GenAI-powered data governance tools, I often struggle with choosing the right chunking approach to balance context retention and latency. Your explanation has given a much clearer decision. I’ll be applying these insights in my upcoming LangChain + Azure GPT workflow!
```

2

Reply

[![Roberto Carlos](https://ddlihl75qpk8y0.archive.is/1nxMc/ad61039933c0030acc8ccdbe2c128060c172b9cb.jpg)](https://archive.is/o/1nxMc/https%3A//medium.com/%40robertocarlos_29501)

[Roberto Carlos](https://archive.is/o/1nxMc/https%3A//medium.com/%40robertocarlos_29501)

[12 hours ago (edited)](https://archive.is/o/1nxMc/https%3A//medium.com/%40robertocarlos_29501/thanks-for-your-article-it-is-great-7c7825fb7cd9)

```
Thanks for your article , it is great. Only I have a question, if you have thousands of documents, how do you choose the Best chunking function? I mean, doing by hand it is imposible.
```

1

Reply

See all responses

## More from Anjolaoluwa Ajayi and AI Advances

![17 Prompt Engineering Techniques and When to Use Them](https://ddlihl75qpk8y0.archive.is/1nxMc/1969e615e25f9c42ed43a77cc803a6b5c8717a15.jpg)

[![AI Advances](https://ddlihl75qpk8y0.archive.is/1nxMc/9665b43a61e485b5c84d91d530a02165bcfe08df.png)](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/)

In

[AI Advances](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/)

by

[Anjolaoluwa Ajayi](https://archive.is/o/1nxMc/https%3A//medium.com/%40dataprincess)

[## 17 Prompt Engineering Techniques and When to Use Them

### From Easy to Advanced with Examples](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/17-prompt-engineering-techniques-and-when-to-use-them-1a42e731dfe5)

Jan 26

[A clap icon1.4K

A response icon12](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/17-prompt-engineering-techniques-and-when-to-use-them-1a42e731dfe5)

![The Hidden Costs of LangChain, CrewAI, PydanticAI and Others: Why Popular AI Frameworks Are Failing…](https://ddlihl75qpk8y0.archive.is/1nxMc/a9f71560c065582c772cb162d7206238a6cbccfc.jpg)

[![AI Advances](https://ddlihl75qpk8y0.archive.is/1nxMc/9665b43a61e485b5c84d91d530a02165bcfe08df.png)](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/)

In

[AI Advances](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/)

by

[Kenny Vaneetvelde](https://archive.is/o/1nxMc/https%3A//medium.com/%40kenny_v)

[## The Hidden Costs of LangChain, CrewAI, PydanticAI and Others: Why Popular AI Frameworks Are Failing…

### After 15 years in software development and countless hours wrestling with AI frameworks, I had reached a breaking point. The promise of…](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/the-hidden-costs-of-langchain-crewai-pydanticai-and-others-why-popular-ai-frameworks-are-failing-77b9a40c16cf)

Jul 13

[A clap icon569

A response icon21](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/the-hidden-costs-of-langchain-crewai-pydanticai-and-others-why-popular-ai-frameworks-are-failing-77b9a40c16cf)

![Agentic AI Lifecycle for Enterprise Processes](https://ddlihl75qpk8y0.archive.is/1nxMc/eb912f15b006a3997f935cc466091aff77bb0572.jpg)

[![AI Advances](https://ddlihl75qpk8y0.archive.is/1nxMc/9665b43a61e485b5c84d91d530a02165bcfe08df.png)](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/)

In

[AI Advances](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/)

by

[Debmalya Biswas](https://archive.is/o/1nxMc/https%3A//debmalyabiswas.medium.com/)

[## Agentic AI Lifecycle for Enterprise Processes

### The art of transforming Manual processes into an Orchestration of AI Agents](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/agentification-of-enterprise-processes-0f173554f7b4)

Jun 29

[A clap icon530

A response icon13](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/agentification-of-enterprise-processes-0f173554f7b4)

![Your Streamlit Apps Don’t Have to Suck](https://ddlihl75qpk8y0.archive.is/1nxMc/67487db884f42aff1c346a691e8c2a7cf97b46d6.png)

[![Level Up Coding](data:image/jpeg;base64...)](https://archive.is/o/1nxMc/https%3A//levelup.gitconnected.com/)

In

[Level Up Coding](https://archive.is/o/1nxMc/https%3A//levelup.gitconnected.com/)

by

[Anjolaoluwa Ajayi](https://archive.is/o/1nxMc/https%3A//medium.com/%40dataprincess)

[## Your Streamlit Apps Don’t Have to Suck

### 6 Simple Ways to Customize Your Streamlit Apps](https://archive.is/o/1nxMc/https%3A//levelup.gitconnected.com/your-streamlit-apps-dont-have-to-suck-02edf452399c)

Feb 14

[A clap icon532

A response icon1](https://archive.is/o/1nxMc/https%3A//levelup.gitconnected.com/your-streamlit-apps-dont-have-to-suck-02edf452399c)

[See all from Anjolaoluwa Ajayi](https://archive.is/o/1nxMc/https%3A//medium.com/%40dataprincess)

[See all from AI Advances](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/)

## Recommended from Medium

![Voxtral : Mistral just killed Whisper for Audio AI](https://ddlihl75qpk8y0.archive.is/1nxMc/3567e90e8778de61a5c947ecedd3d9387316a3e3.jpg)

[![Data Science in Your Pocket](https://ddlihl75qpk8y0.archive.is/1nxMc/b4738e2921ba4f4056f39e9d948994bdea212380.jpg)](https://archive.is/o/1nxMc/https%3A//medium.com/data-science-in-your-pocket)

In

[Data Science in Your Pocket](https://archive.is/o/1nxMc/https%3A//medium.com/data-science-in-your-pocket)

by

[Mehul Gupta](https://archive.is/o/1nxMc/https%3A//medium.com/%40mehulgupta_7991)

[## Voxtral : Mistral just killed Whisper for Audio AI

### Mistral new open-source Audio AI model](https://archive.is/o/1nxMc/https%3A//medium.com/data-science-in-your-pocket/voxtral-mistral-just-killed-whisper-for-audio-ai-82b6ad3a7596)

4d ago

[A clap icon244

A response icon1](https://archive.is/o/1nxMc/https%3A//medium.com/data-science-in-your-pocket/voxtral-mistral-just-killed-whisper-for-audio-ai-82b6ad3a7596)

![Building MCP-Powered Agentic RAG Application: Step-by-Step Guide (1/2)](https://ddlihl75qpk8y0.archive.is/1nxMc/9f5ab604ebaef2177a4d49e5209d16f181d3b654.png)

[![Level Up Coding](data:image/jpeg;base64...)](https://archive.is/o/1nxMc/https%3A//levelup.gitconnected.com/)

In

[Level Up Coding](https://archive.is/o/1nxMc/https%3A//levelup.gitconnected.com/)

by

[Youssef Hosni](https://archive.is/o/1nxMc/https%3A//yousefhosni.medium.com/)

[## Building MCP-Powered Agentic RAG Application: Step-by-Step Guide (1/2)

### A Step-by-Step Guide to Building an Agentic RAG Application with MCP](https://archive.is/o/1nxMc/https%3A//levelup.gitconnected.com/building-mcp-powered-agentic-rag-application-step-by-step-guide-1-2-efea9fb6f250)

Jul 14

[A clap icon824

A response icon4](https://archive.is/o/1nxMc/https%3A//levelup.gitconnected.com/building-mcp-powered-agentic-rag-application-step-by-step-guide-1-2-efea9fb6f250)

![RAG is Not Enough: Why Your Next AI Project Demands Structured Data RAG](https://ddlihl75qpk8y0.archive.is/1nxMc/7ca4e76433b96bdbbe057cb1dacb3d35dcaee25d.png)

[![Data And Beyond](data:image/jpeg;base64...)](https://archive.is/o/1nxMc/https%3A//medium.com/data-and-beyond)

In

[Data And Beyond](https://archive.is/o/1nxMc/https%3A//medium.com/data-and-beyond)

by

[Chinmay Bhalerao](https://archive.is/o/1nxMc/https%3A//medium.com/%40BH_Chinmay)

[## RAG is Not Enough: Why Your Next AI Project Demands Structured Data RAG

### The FAST-RAG system without complex embedding models or vector databases](https://archive.is/o/1nxMc/https%3A//medium.com/data-and-beyond/rag-is-not-enough-why-your-next-ai-project-demands-structured-data-rag-9562c8fc3a8b)

Jul 9

[A clap icon273

A response icon2](https://archive.is/o/1nxMc/https%3A//medium.com/data-and-beyond/rag-is-not-enough-why-your-next-ai-project-demands-structured-data-rag-9562c8fc3a8b)

![The Hidden Costs of LangChain, CrewAI, PydanticAI and Others: Why Popular AI Frameworks Are Failing…](https://ddlihl75qpk8y0.archive.is/1nxMc/a9f71560c065582c772cb162d7206238a6cbccfc.jpg)

[![AI Advances](https://ddlihl75qpk8y0.archive.is/1nxMc/9665b43a61e485b5c84d91d530a02165bcfe08df.png)](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/)

In

[AI Advances](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/)

by

[Kenny Vaneetvelde](https://archive.is/o/1nxMc/https%3A//medium.com/%40kenny_v)

[## The Hidden Costs of LangChain, CrewAI, PydanticAI and Others: Why Popular AI Frameworks Are Failing…

### After 15 years in software development and countless hours wrestling with AI frameworks, I had reached a breaking point. The promise of…](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/the-hidden-costs-of-langchain-crewai-pydanticai-and-others-why-popular-ai-frameworks-are-failing-77b9a40c16cf)

Jul 13

[A clap icon569

A response icon21](https://archive.is/o/1nxMc/https%3A//ai.gopubby.com/the-hidden-costs-of-langchain-crewai-pydanticai-and-others-why-popular-ai-frameworks-are-failing-77b9a40c16cf)

![Why Japanese Developers Write Code Completely Differently (And Why It Works Better)](https://ddlihl75qpk8y0.archive.is/1nxMc/0c4d8ce52321dd5d8faa003184d0fdeb320b06cf.jpg)

[![Sohail Saifi](data:image/jpeg;base64...)](https://archive.is/o/1nxMc/https%3A//medium.com/%40sohail_saifi)

[Sohail Saifi](https://archive.is/o/1nxMc/https%3A//medium.com/%40sohail_saifi)

[## Why Japanese Developers Write Code Completely Differently (And Why It Works Better)

### I’ve been studying Japanese software development practices for the past three years, and what I discovered completely changed how I think…](https://archive.is/o/1nxMc/https%3A//medium.com/%40sohail_saifi/why-japanese-developers-write-code-completely-differently-and-why-it-works-better-de84d6244fab)

4d ago

[A clap icon4.4K

A response icon129](https://archive.is/o/1nxMc/https%3A//medium.com/%40sohail_saifi/why-japanese-developers-write-code-completely-differently-and-why-it-works-better-de84d6244fab)

![How I Built a Custom AI Document Assistant That Understands 1000s of PDFs and Talks Like a Human](https://ddlihl75qpk8y0.archive.is/1nxMc/3be1d456d2cfe9a13999898fd147e09011d7124a.jpg)

[![Stackademic](https://ddlihl75qpk8y0.archive.is/1nxMc/deeac06961714364fb600961b3f9ca13a99f4e20.png)](https://archive.is/o/1nxMc/https%3A//blog.stackademic.com/)

In

[Stackademic](https://archive.is/o/1nxMc/https%3A//blog.stackademic.com/)

by

[Abdul Ahad](https://archive.is/o/1nxMc/https%3A//medium.com/%40abdul.ahadmahmood555)

[## How I Built a Custom AI Document Assistant That Understands 1000s of PDFs and Talks Like a Human

### Forget basic search. I designed a Retrieval-Augmented Generation (RAG) system that reads technical documents, extracts diagrams, interprets…](https://archive.is/o/1nxMc/https%3A//blog.stackademic.com/how-i-built-a-custom-ai-document-assistant-that-understands-1000s-of-pdfs-and-talks-like-a-human-ec3aa57f370f)

Jul 3

[A clap icon576

A response icon16](https://archive.is/o/1nxMc/https%3A//blog.stackademic.com/how-i-built-a-custom-ai-document-assistant-that-understands-1000s-of-pdfs-and-talks-like-a-human-ec3aa57f370f)

[See more recommendations](https://archive.is/o/1nxMc/https%3A//medium.com/)

[Help](https://archive.is/o/1nxMc/https%3A//help.medium.com/hc/en-us)

[Status](https://archive.is/o/1nxMc/https%3A//medium.statuspage.io/)

[About](https://archive.is/o/1nxMc/https%3A//medium.com/about)

[Careers](https://archive.is/o/1nxMc/https%3A//medium.com/jobs-at-medium/work-at-medium-959d1a85284e)

Press

[Blog](https://archive.is/o/1nxMc/https%3A//blog.medium.com/)

[Privacy](https://archive.is/o/1nxMc/https%3A//policy.medium.com/medium-privacy-policy-f03bf92035c9)

[Rules](https://archive.is/o/1nxMc/https%3A//policy.medium.com/medium-rules-30e5502c4eb4)

[Terms](https://archive.is/o/1nxMc/https%3A//policy.medium.com/medium-terms-of-service-9db0094a1e0f)

[Text to speech](https://archive.is/o/1nxMc/https%3A//speechify.com/medium)

|  |
| --- |
| [0%](https://archive.is/20250722111301/https%3A//ai.gopubby.com/21-chunking-strategies-for-rag-f28e4382d399#0%) |
|  |
| [10%](https://archive.is/20250722111301/https%3A//ai.gopubby.com/21-chunking-strategies-for-rag-f28e4382d399#10%) |
|  |
| [20%](https://archive.is/20250722111301/https%3A//ai.gopubby.com/21-chunking-strategies-for-rag-f28e4382d399#20%) |
|  |
| [30%](https://archive.is/20250722111301/https%3A//ai.gopubby.com/21-chunking-strategies-for-rag-f28e4382d399#30%) |
|  |
| [40%](https://archive.is/20250722111301/https%3A//ai.gopubby.com/21-chunking-strategies-for-rag-f28e4382d399#40%) |
|  |
| [50%](https://archive.is/20250722111301/https%3A//ai.gopubby.com/21-chunking-strategies-for-rag-f28e4382d399#50%) |
|  |
| [60%](https://archive.is/20250722111301/https%3A//ai.gopubby.com/21-chunking-strategies-for-rag-f28e4382d399#60%) |
|  |
| [70%](https://archive.is/20250722111301/https%3A//ai.gopubby.com/21-chunking-strategies-for-rag-f28e4382d399#70%) |
|  |
| [80%](https://archive.is/20250722111301/https%3A//ai.gopubby.com/21-chunking-strategies-for-rag-f28e4382d399#80%) |
|  |
| [90%](https://archive.is/20250722111301/https%3A//ai.gopubby.com/21-chunking-strategies-for-rag-f28e4382d399#90%) |
|  |
| [100%](https://archive.is/20250722111301/https%3A//ai.gopubby.com/21-chunking-strategies-for-rag-f28e4382d399#100%) |
