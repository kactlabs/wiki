/ [Home](index.md)

## Template

**Note:** tbw




```
🔟 𝗜𝗻𝗴𝗲𝘀𝘁𝗶𝗼𝗻 & 𝗙𝗹𝗼𝘄 𝗖𝗼𝗻𝘁𝗿𝗼𝗹 (optional but critical)
→ Accept scans, PDFs, mobile uploads
→ Split to page-level images
→ Use FastAPI, Ray, or Prefect for routing, batching, and retries

9️⃣ 𝗣𝗼𝘀𝘁𝗽𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 & 𝗙𝗶𝗲𝗹𝗱 𝗟𝗼𝗴𝗶𝗰
→ IOU merging, box clustering, regex cleanup, spatial grouping
→ LM sanity checks, box confidence filtering
→ Outputs as clean JSON, DB inserts, or downstream API payloads

8️⃣ 𝗟𝗮𝘆𝗼𝘂𝘁 𝗔𝗻𝗮𝗹𝘆𝘀𝗶𝘀
→ doclayout-yolo, PubLayNet, LayoutParser, TableNet, FastDoc
→ Detect headers, tables, stamps, and multi-column zones
→ Layout adds structure when raw text isn’t enough

7️⃣ 𝗢𝗖𝗥 𝗘𝗻𝗴𝗶𝗻𝗲𝘀
→ PaddleOCR, docTR, EasyOCR, TroCR, Tesseract, Surya, OLM-OCR
→ OCR output should include:
• Page number
• Bounding boxes
• Confidence scores
→ This metadata preserves layout structure and document flow

6️⃣ 𝗣𝗿𝗲𝗽𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴
→ OpenCV, CLAHE, deskewing, adaptive thresholding
→ Despeckle, denoise, DPI normalization
→ Clean inputs = stronger OCR and VLM output

5️⃣ 𝗙𝗶𝗲𝗹𝗱 𝗘𝘅𝘁𝗿𝗮𝗰𝘁𝗶𝗼𝗻
→ LayoutLMv3, Donut, spaCy, transformers, TranKIT
→ Or use small LLMs (e.g. LLaMA3 8B) with structured prompts on OCR’d text
→ Doesn’t require full VLM inference — fast and domain-adaptable

4️⃣ 𝗥𝗲𝘁𝗿𝗶𝗲𝘃𝗮𝗹 (𝗥𝗔𝗚)
→ LlamaIndex, LangChain, FAISS, Qdrant, Weaviate, Milvus
→ Layout-aware chunking > flat text splits
→ Crucial for relevance, especially with multi-page documents

3️⃣ 𝗟𝗟𝗠𝘀 / 𝗩𝗤𝗔 / 𝗩𝗟𝗠𝘀
→ GPT-4o, Claude 3, PaLI, ColPaLI, Kosmos-2, BLIP-2, LLaVA
→ Understand scanned charts, tables, handwriting
→ Unlock reasoning where OCR-only fails

2️⃣ 𝗘𝘃𝗮𝗹𝘂𝗮𝘁𝗶𝗼𝗻 / 𝗤𝗔
→ Ragas, DeepEval, OCR eval (box-level thresholds), hallucination detection
→ Retrieval scoring, confidence auditing, prompt failure analysis
→ Evaluation isn’t a step, it’s a loop

1️⃣ 𝗗𝗲𝗽𝗹𝗼𝘆𝗺𝗲𝗻𝘁 & 𝗥𝘂𝗻𝘁𝗶𝗺𝗲
→ LangServe, FastAPI, Ray, Docker, Prefect
→ Needed for scale, retries, fallback routing, observability
→ Treat your pipeline like a real service, not a script

📌 Most teams either overcomplicate or oversimplify.

The best pipelines blend OCR + CV + LLMs into a layout-aware stack.


```


![alt text](image-19.png)