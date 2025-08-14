/ [Home](index.md)

## GenAI Roadmap for 2026

**Note:** Learn GenAI in 2026


---

## Level 1 — Foundations of GenAI and Transformers
- What is Generative AI, and how it’s different from traditional ML  
- Transformer architecture (attention, positional encoding, decoder stacks)  
- Tokens, embeddings, and positional context  
- Pretraining vs fine-tuning vs instruction tuning  
- Inference with pre-trained models (e.g., LLaMA, Mistral, Mixtral, Phi-3)  
- Understanding tokenization and model vocabulary (e.g., SentencePiece, BPE)  

---

## Level 2 — Language Model Behavior and Prompting
- Prompt engineering basics (zero-shot, few-shot, CoT, ReAct)  
- Role prompting, context design, and persona injection  
- Advanced prompting methods (Tree-of-Thought, Graph-of-Thought, WebGPT)  
- Temperature, top-k, top-p, beam search — decoding strategies  
- Prompt compression and optimization techniques  
- Guardrails and adversarial prompting defense (OpenAI function calling guardrails, NeMo Guardrails)  

---

## Level 3 — Retrieval-Augmented Generation (RAG)
- What is RAG and when to use it  
- Chunking strategies (semantic, fixed size, recursive)  
- Embedding models (OpenAI, Cohere, BGE, E5, GTE, Jina Embeddings)  
- Vector DBs (FAISS, Weaviate, Qdrant, LanceDB, PGVector)  
- RAG pipelines (SimpleRAG, Multi-RAG, HybridRAG, GraphRAG)  
- Evaluating RAG output (faithfulness, hallucination, groundedness)  
- Fine-tuning embedding models for retrieval (contrastive learning)  

---

## Level 4 — LLMOps and Tool Integration
- Intro to LLMOps vs MLOps  
- LangChain, LlamaIndex, Dust, Haystack, Marvin, CrewAI  
- LangGraph: event-driven, graph-based agent workflows  
- Tool calling with OpenAI (function calling, JSON mode, tool_choice)  
- Auto tool selection and dynamic routing  
- OpenAI tool integration vs Anthropic tool use  
- Synthetic data generation using agents  

---

## Level 5 — Agents and Agentic Frameworks
- What are agents and why do we need them  
- Types of agents (tool-using, multi-hop, planning, recursive)  
- ReAct vs Plan-and-Solve vs AutoGPT-style agents  
- Action-observation loops and memory grounding  
- Simple agent construction using LangChain Agents  
- Building autonomous loops with LangGraph, CrewAI, and MetaGPT  
- Autonomous evaluation loops using LM-as-a-Judge  

---

## Level 6 — Agent Memory, State & Orchestration
- Types of memory: Buffer, Summary, Entity, Vector  
- Episodic vs persistent memory  
- Context window strategies and context compression  
- Memory via Redis, Chroma, or LangChain Memory classes  
- Event-driven memory updates in LangGraph  
- Function calling-based memory updates  
- Combining symbolic memory with vector memory for reasoning agents  

---

## Level 7 — Multi-Agent Systems and Collaboration
- What is multi-agent collaboration and when it matters  
- Architectures: Hub-and-Spoke, Decentralized, Hierarchical  
- Message passing and communication protocols  
- Multi-agent planning (e.g., CrewAI, AutoGen, DSPy teams)  
- Conflict resolution and alignment in agent teams  
- Applications: agents as research assistants, financial bots, dev teams  
- Agent grading and self-play loops for training  

---

## Level 8 — Evaluation, Feedback Loops, and RL
- LM-as-a-Judge (LUNA-2, OpenAI Evals, Anthropic Claude Evaluator)  
- Pairwise and unary comparison techniques  
- Building reward models from user preferences  
- RLHF, RLAIF, and RLVR — when and how to apply  
- Grading reasoning chains with teacher verifiers  
- Supervised fine-tuning on evaluator-graded data  
- Using feedback signals to retrain agents in production  

---

## Level 9 — Protocols, Safety, and Advanced Alignment
- Model Context Protocol (MCP) and how it structures agent memory  
- Action-to-Action Protocol (A2A) for autonomous agents  
- Safety-first designs: Constitutional AI, verifiable agents, red teaming  
- Traceability and logging in LangGraph/LLMOps stacks  
- Guardrails and safe output validation (Nvidia NeMo Guardrails, GuardrailsAI)  
- Autonomous policy updates through inner-loop retraining  
- Self-verifying agents for open-ended generation  

---

## Level 10 — Build, Optimize & Deploy in Production
- App frameworks: Gradio, Streamlit, Dash, Chainlit  
- Serving agents: FastAPI, Modal, Replicate, RunPod  
- Quantization and model compression (GGUF, QLoRA, AWQ)  
- Cost optimization using small language models (Phi-3, TinyLlama)  
- Infrastructure: Docker, serverless agents, GPUs vs CPUs  
- Prompt caching and vector cache optimization  
- Observability: LangSmith, Arize, Trulens, Weights & Biases  
