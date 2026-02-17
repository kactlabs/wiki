/ [Home](index.md)

## ReRanking Algorithms

# Advanced Re-Ranking Techniques in Modern Retrieval Systems

Re-ranking is the **second-stage optimization layer** in multi-stage retrieval pipelines (e.g., BM25 → ANN → Re-ranker → LLM).  
Its purpose is to improve **precision@k, nDCG, MRR**, and reduce hallucination risk in RAG systems.

---

# 1. MMR (Maximal Marginal Relevance)

## Concept

**Maximal Marginal Relevance (MMR)** balances:

- Query relevance
- Inter-document diversity

It prevents near-duplicate documents from dominating top-k results.

## Formula

\[
MMR = \arg\max_{D_i \in R \setminus S}
\left[
\lambda \cdot Sim(D_i, Q)
-
(1-\lambda) \cdot \max_{D_j \in S} Sim(D_i, D_j)
\right]
\]

Where:

- `Q` = query
- `R` = candidate set
- `S` = selected documents
- `λ` = relevance/diversity tradeoff (0–1)

## Characteristics

- Lightweight (no model inference required)
- Works on embedding similarity
- Improves contextual coverage in RAG

## Limitations

- Greedy heuristic
- Not learned
- Pairwise only (no global structure)

---

# 2. Cross-Encoder Re-Ranking (Neural Rerankers)

## Concept

Unlike bi-encoders (separate embeddings), **cross-encoders** process:
[CLS] Query [SEP] Document
in a single transformer forward pass.

## Architecture

- Typically BERT / RoBERTa style encoder
- Classification head outputs relevance score

## Strengths

- Superior ranking quality
- Captures fine-grained token interactions
- Strong performance on MS MARCO benchmarks

## Weaknesses

- Expensive (O(k) forward passes)
- Not scalable for large candidate pools

## Common Models

- `cross-encoder/ms-marco-MiniLM-L-6-v2`
- MonoBERT
- MonoT5

## Typical Pipeline

Stage 1: Retrieve top-100 via BM25/ANN  
Stage 2: Re-rank top-100 via cross-encoder  
Stage 3: Select top-5 for LLM context

---

# 3. Neural Diversity Rerankers (Beyond MMR)

## Concept

Learned models that optimize both:

- Relevance
- Diversity
- Subtopic coverage

Instead of heuristic diversity (MMR), these use neural learning.

## Methods

### Determinantal Point Processes (DPP)
Encourages diverse subset selection via determinant maximization.

### xQuAD
Explicitly models query subtopics.

### Neural Subtopic Modeling
Transformer-based diversity scoring.

## Strengths

- Better subtopic coverage
- Useful for exploratory search
- Reduces redundancy in RAG

## Limitations

- More complex
- Harder to train
- Requires labeled data with subtopics

---

# 4. Transformer-Based Generative Retrieval  
(GenRE / SEAL / SPLADE / ColBERTv2)

These blur the boundary between retrieval and generation.

---

## 4.1 GenRE (Generative Retrieval)

### Concept

Model directly **generates document IDs** given a query.
Query → Transformer → DocID tokens

### Pros

- No vector DB needed
- Fully differentiable
- End-to-end training

### Cons

- Scaling issues
- Requires retraining for corpus updates

---

## 4.2 SEAL

SEAL encodes documents as token sequences and retrieves via generation.

- Jointly learns retrieval
- Handles long-tail better than sparse models

---

## 4.3 SPLADE

Sparse lexical expansion via transformer.

- Produces sparse vectors
- Retains inverted-index compatibility
- Strong BM25 replacement

Advantages:
- Efficient
- Hybrid lexical + semantic behavior

---

## 4.4 ColBERTv2

Late-interaction architecture:

- Query and doc encoded separately
- Token-level max-sim interaction
- Efficient approximate search

Advantages:
- Higher precision than bi-encoder
- More scalable than cross-encoder

---

# 5. Learned Global Reranking Frameworks

## Concept

Instead of scoring independently, model:

- Entire candidate list
- Global ranking order

## Techniques

### Listwise Learning-to-Rank

- LambdaMART
- ListNet
- ListMLE

### Transformer Listwise Models

- Encode entire document list jointly
- Optimize nDCG directly

## Benefits

- Captures inter-document competition
- Better global ordering
- Optimizes ranking metrics explicitly

## Challenges

- Computationally heavy
- Complex training pipeline

---

# 6. LLM-Centric Reranking  
(In-Context / Prompt-Based Rerankers)

## Concept

Use a Large Language Model to rank candidate documents via prompting.

Example:

Given query Q and documents D1…D5,
rank them by relevance.

## Methods

### Score-based Prompting
LLM outputs relevance score.

### Pairwise Comparison
LLM compares D1 vs D2 iteratively.

### Chain-of-Thought Ranking
LLM explains ranking before output.

## Strengths

- Strong reasoning capability
- No task-specific training required
- Adapts to domain via prompt engineering

## Weaknesses

- Expensive
- Latency heavy
- Not deterministic
- Hard to calibrate scores

---

# Comparative Summary

| Method | Learning-Based | Scalable | Diversity-Aware | Precision | Cost |
|--------|----------------|----------|-----------------|-----------|------|
| MMR | ❌ | ✅ | ✅ | Medium | Low |
| Cross-Encoder | ✅ | ❌ | ❌ | High | High |
| Neural Diversity | ✅ | ⚠️ | ✅ | High | Medium |
| GenRE / SEAL | ✅ | ❌ | ❌ | High | High |
| SPLADE | ✅ | ✅ | ❌ | High | Medium |
| ColBERTv2 | ✅ | ✅ | ❌ | High | Medium |
| Global Listwise | ✅ | ❌ | ⚠️ | Very High | High |
| LLM Reranking | ❌ (usually) | ❌ | ⚠️ | Very High | Very High |

---

# When to Use What (RAG Engineering View)

- Small system, need diversity → **MMR**
- Production RAG, high precision → **Cross-Encoder**
- Hybrid lexical-semantic → **SPLADE**
- High-performance scalable retrieval → **ColBERTv2**
- Research / end-to-end retrieval → **GenRE**
- Multi-document reasoning → **LLM reranking**
- Search engine optimization → **Listwise learning-to-rank**

---

# Final Engineering Principle

> Retrieval quality impacts hallucination rate more than model size.

Re-ranking is not an optimization detail —  
it is a **core reliability mechanism** in modern LLM systems.