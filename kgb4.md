/ [Home](index.md)

## Kactii GenAI Bootcamp - Season 4 / S4

**Note:** Military Style Gamified Learning Framework

### Syllabus
Updated: March 1, 2025

**Chapter 1: Introduction to GenAI Engineering**
Start your journey into GenAI engineering. Understand the key concepts and tools used in the industry. Gain a comprehensive overview of AI and machine learning technologies. Set the stage for advanced learning and practical application. Lay a strong foundation for your GenAI career.

**Chapter 2: Large Language Models (LLM) Fundamentals**
Dive deep into Large Language Models including OpenAI GPT series, Claude (Anthropic), Gemini (Google), and Llama Family (Meta). Understand model architectures, training processes, and capabilities. Learn prompt engineering, fine-tuning techniques, and model selection strategies for different use cases.

**Chapter 3: LangChain Ecosystem Mastery**
Master the complete LangChain ecosystem including LangChain core framework, LangGraph for graph-based workflows, LangFuse for observability and analytics, and LangSmith for development and debugging. Build complex AI applications with chain-of-thought reasoning and multi-step workflows.

**Chapter 4: Vector Databases and Embeddings**
Master vector databases including Qdrant, Weaviate, FAISS, Milvus, and Chroma for AI-native applications. Learn embedding techniques, similarity search, and retrieval-augmented generation (RAG). Implement semantic search, document retrieval, and knowledge base systems for GenAI applications.

**Chapter 5: Model Context Protocol (MCP) and Agent-to-Agent Communication**
Learn Model Context Protocol for standardized AI model communication and Agent-to-Agent (A2A) communication patterns. Implement multi-agent systems, orchestrate complex workflows, and build collaborative AI applications. Master inter-agent messaging, task delegation, and distributed AI processing.

**Chapter 6: Local LLM Deployment with Ollama**
Master local LLM deployment using Ollama for privacy-focused and cost-effective AI applications. Learn model quantization, optimization techniques, and hardware requirements. Implement offline AI capabilities, custom model fine-tuning, and edge deployment strategies for production environments.

**Chapter 7: HuggingFace Ecosystem and Model Hub**
Master the HuggingFace ecosystem for model deployment, sharing, and collaboration. Learn to use Transformers library, Datasets, and Spaces for building and deploying AI applications. Implement model fine-tuning, dataset preparation, and community collaboration through the HuggingFace platform.

**Chapter 8: Database Technologies for GenAI Applications**
Master multiple database technologies including MongoDB, PostgreSQL with SQLAlchemy and Alembic, Supabase, and SQLiteDB. Learn to design data architectures for AI applications, implement database migrations, and optimize queries for large-scale GenAI systems with proper data modelling.

**Chapter 9: Workflow Orchestration and Background Processing**
Master workflow orchestration using Prefect and background job processing with Dramatiq for scalable GenAI applications. Learn to design complex AI pipelines, handle asynchronous tasks, and implement distributed processing systems for production-grade AI workflows.

**Chapter 10: Interactive Development with Notebook LLM and PyNotes**
Master interactive development environments using Notebook LLM for AI experimentation and PyNotes for technical documentation. Learn to create reproducible research notebooks, document AI experiments, and build interactive AI prototypes using modern notebook-based development workflows.

**Chapter 11: Alternative GenAI Frameworks and Haystack**
Explore alternative GenAI frameworks beyond LangChain, focusing on Haystack NLP pipeline framework. Learn to build production-ready NLP applications, implement custom components, and compare different framework approaches for various GenAI use cases and requirements.

**Chapter 12: Research Publication and Portfolio Development**
Complete your GenAI journey by publishing 1-3 research papers on ArXiv and building a comprehensive portfolio. Learn academic writing, research methodologies, and publication processes. Create projects for GitHub, GitBook documentation, Google Colab notebooks, and HuggingFace model sharing to showcase your expertise.



---

### Weekly Sessions

# Kactii GenAI Bootcamp S4 — 12-Week Master Plan
> **Model Provider:** llama.cpp (local, no cloud API keys)  
> **Hardware:** RTX 3090 (24GB VRAM) + Ubuntu  
> **Structure:** 12 Chapters × 5 Sessions = 60 Sessions

---

## Week 1 — GenAI Engineering Foundations
*Chapter 1: Introduction to GenAI Engineering*

| Day | Topic |
|-----|-------|
| 1 | Install llama.cpp from source, download first GGUF, run CLI inference |
| 2 | llama.cpp server mode, hit `/v1/chat/completions` via curl + Python |
| 3 | Tokenization hands-on with `llama-tokenize`, context window experiments |
| 4 | GGUF format deep dive, quantization types (Q4 vs Q5 vs Q8) comparison |
| 5 | Build reusable `LlamaCppClient` Python class used throughout the bootcamp |

---

## Week 2 — LLM Fundamentals
*Chapter 2: Large Language Models (LLM) Fundamentals*

| Day | Topic |
|-----|-------|
| 6 | Model families survey (GPT, Claude, Gemini, Llama) — run two GGUFs side-by-side |
| 7 | Zero-shot vs few-shot prompting harness in Python |
| 8 | Chain-of-thought + Jinja2 system prompt templating |
| 9 | LoRA/QLoRA concepts — compare base vs fine-tuned GGUF on domain task |
| 10 | Model selection mini project: pick the right GGUF for 3 different task briefs |

---

## Week 3 — LangChain Ecosystem
*Chapter 3: LangChain Ecosystem Mastery*

| Day | Topic |
|-----|-------|
| 11 | Wire LangChain `ChatOpenAI` to llama.cpp via `base_url` override |
| 12 | Build LCEL chains: prompt template → model → output parser |
| 13 | LangGraph intro — build a simple `StateGraph` with two nodes |
| 14 | LangSmith local tracing — log chain execution without cloud dependency |
| 15 | Multi-step workflow: LangGraph agent with conditional edges + llama.cpp brain |

---

## Week 4 — Vector Databases & Embeddings
*Chapter 4: Vector Databases and Embeddings*

| Day | Topic |
|-----|-------|
| 16 | Embedding concepts — use llama.cpp `/v1/embeddings` with a local embedding GGUF |
| 17 | FAISS hands-on: index documents, run similarity search manually |
| 18 | Qdrant via Docker — upsert vectors, metadata filtering, compare recall vs FAISS |
| 19 | Full RAG pipeline: loader → chunker → Qdrant retriever → llama.cpp LLM |
| 20 | RAG evaluation: chunk size tuning, hallucination on low-recall queries, mini project |

---

## Week 5 — MCP & Agent-to-Agent Communication
*Chapter 5: Model Context Protocol (MCP) and Agent-to-Agent Communication*

| Day | Topic |
|-----|-------|
| 21 | MCP protocol concepts — build a minimal MCP server with `fastmcp` |
| 22 | Register tools on MCP server, connect client to llama.cpp endpoint |
| 23 | Tool-call JSON parsing from raw GGUF output — structured outputs with Pydantic |
| 24 | A2A pattern: Orchestrator + Specialist agents communicating over HTTP |
| 25 | Multi-agent mini project: two llama.cpp-powered agents solve a task collaboratively |

---

## Week 6 — Local LLM Deployment & Optimization
*Chapter 6: Local LLM Deployment with Ollama*

| Day | Topic |
|-----|-------|
| 26 | llama.cpp GPU offloading — tune `-ngl` layers on RTX 3090, measure VRAM usage |
| 27 | Convert HuggingFace model to GGUF using `convert_hf_to_gguf.py` |
| 28 | Quantize to Q4/Q5/Q8 — benchmark tokens/sec and perplexity tradeoffs |
| 29 | Serve multiple models with `llama-server` — model switching strategies |
| 30 | Edge deployment simulation: run llama.cpp on CPU-only Ubuntu laptop, compare perf |

---

## Week 7 — HuggingFace Ecosystem
*Chapter 7: HuggingFace Ecosystem and Model Hub*

| Day | Topic |
|-----|-------|
| 31 | HuggingFace Hub tour — find, download, and convert models to GGUF locally |
| 32 | Transformers library: run inference locally, compare output vs llama.cpp GGUF |
| 33 | Dataset preparation with HuggingFace `datasets` for fine-tuning input |
| 34 | Fine-tune a small model with LoRA using `peft` + push adapter to HF Hub |
| 35 | Convert fine-tuned adapter to GGUF — serve it via llama.cpp, validate output |

---

## Week 8 — Database Technologies
*Chapter 8: Database Technologies for GenAI Applications*

| Day | Topic |
|-----|-------|
| 36 | MongoDB for chat history — store and retrieve conversation turns for llama.cpp context |
| 37 | PostgreSQL + SQLAlchemy: design schema for agent memory and task logs |
| 38 | Alembic migrations — version your DB schema as your agent app evolves |
| 39 | Supabase as a backend: vector extension + REST API for a RAG app |
| 40 | Multi-DB mini project: agent uses Mongo for memory, Postgres for structured logs |

---

## Week 9 — Workflow Orchestration
*Chapter 9: Workflow Orchestration and Background Processing*

| Day | Topic |
|-----|-------|
| 41 | Prefect intro — wrap RAG pipeline as a Prefect flow with tasks |
| 42 | Schedule and deploy a Prefect flow: nightly document re-indexing job |
| 43 | Dramatiq for async background jobs — trigger embedding on new file drop |
| 44 | Error handling and retries in Prefect + Dramatiq for flaky llama.cpp calls |
| 45 | End-to-end orchestrated pipeline: ingest → embed → query → log, fully automated |

---

## Week 10 — Interactive Development & Documentation
*Chapter 10: Interactive Development with Notebook LLM and PyNotes*

| Day | Topic |
|-----|-------|
| 46 | Jupyter + llama.cpp: build a reproducible experiment notebook |
| 47 | PyNotes for technical documentation — document your RAG and agent experiments |
| 48 | Notebook-driven prototyping: iterate on prompts and chains inside Jupyter |
| 49 | Build an interactive demo notebook: upload a PDF, query it via llama.cpp RAG |
| 50 | Portfolio notebook: clean, annotated, shareable on GitHub + Google Colab |

---

## Week 11 — Alternative Frameworks & Haystack
*Chapter 11: Alternative GenAI Frameworks and Haystack*

| Day | Topic |
|-----|-------|
| 51 | Haystack intro — `OpenAIChatGenerator` pointed at llama.cpp server |
| 52 | Build a Haystack document store + retriever + generator pipeline |
| 53 | Custom Haystack components — write a `LlamaCppEmbedder` component |
| 54 | LangChain vs Haystack side-by-side: same RAG task, both frameworks, compare DX |
| 55 | Haystack mini project: production-ready NLP pipeline with llama.cpp backend |

---

## Week 12 — Research, Portfolio & Capstone
*Chapter 12: Research Publication and Portfolio Development*

| Day | Topic |
|-----|-------|
| 56 | arXiv paper structure — abstract, methodology, experiments, results |
| 57 | Pick a paper topic from your bootcamp work (RAG eval, agent benchmarks, etc.) |
| 58 | Capstone build: LangGraph agent + Qdrant RAG + MCP tools + Mongo memory, all on llama.cpp |
| 59 | Deploy capstone as a FastAPI service — GitBook docs + HuggingFace model card |
| 60 | Demo day: present capstone + paper draft to cohort, peer review, submission prep |

---

*60 sessions · 12 weeks · 1 model provider — llama.cpp*



## Project Ideas

| # | Project Idea | Repo |
|---|---|---|
| 1 | Cricket Commentary with LLM | |
| 2 | Stock Market | |
| 3 | 2 Comedians Conversation | |
| 4 | VP and Head of Corporate - Conversation | |
| 5 | Karaoke Judge | [karaoke-icycup-scoring-engine](https://github.com/kactlabs/karaoke-icycup-scoring-engine) |
| 6 | Badminton Judge | |
| 7 | Tennis Judge | |