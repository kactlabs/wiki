/ [Home](index.md)

## GPU Compare

---

## GPU Instance Pricing & Specifications

| GPU Model         | RunPod Price (USD/hr) | VRAM  | System RAM | vCPU | Max Instances | Availability    |
| ----------------- | -------------- | ----- | ---------- | ---- | ------------- | --------------- |
| RTX 4000 Ada SFF  | $0.18/hr       | 20 GB | 35 GB      | 8    | 4             | Low             |
| RTX 4070 Ti       | $0.19/hr       | 12 GB | 30 GB      | 8    | 2             | Low             |
| RTX 4000 Ada      | $0.20/hr       | 20 GB | 31 GB      | 4    | 8             | Low             |
| RTX 4080          | $0.27/hr       | 16 GB | 22 GB      | 8    | 2             | Low             |
| RTX 4080 SUPER    | $0.28/hr       | 16 GB | 41 GB      | 9    | 6             | Low             |
| RTX 4090          | $0.34/hr       | 24 GB | 29 GB      | 6    | 8             | **High**        |
| RTX 5080          | $0.39/hr       | 16 GB | 30 GB      | 8    | 4             | Low             |
| L40               | $0.69/hr       | 48 GB | 125 GB     | 9    | 5             | Low             |
| RTX 6000 Ada      | $0.74/hr       | 48 GB | 109 GB     | 24   | 6             | Low             |
| L40S              | $0.79/hr       | 48 GB | 251 GB     | 24   | 8             | Low             |
| RTX PRO 6000 MaxQ | $0.00/hr       | 96 GB | —          | —    | 7             | **Unavailable** |
| RTX PRO 6000 WK   | $1.69/hr       | 96 GB | 125 GB     | 12   | 4             | Low             |
| RTX PRO 6000      | $1.70/hr       | 96 GB | 125 GB     | 14   | 7             | Low             |
| H100 PCIe         | $1.99/hr       | 80 GB | 251 GB     | 64   | 1             | Low             |
| H100 NVL          | $2.59/hr       | 94 GB | 150 GB     | 19   | 10            | Low             |
| H100 SXM          | $2.69/hr       | 80 GB | 251 GB     | 24   | 8             | Low             |

---

## Notes & Observations

* **Best price-to-performance (consumer GPUs):**

  * RTX 4090 stands out with **High availability** and strong VRAM at $0.34/hr.
* **Best low-cost inference/testing options:**

  * RTX 4000 Ada SFF
  * RTX 4070 Ti
* **Large-model / fine-tuning capable (48–96 GB VRAM):**

  * L40, L40S
  * RTX 6000 Ada
  * RTX PRO 6000 variants
* **Enterprise / large-scale training:**

  * H100 PCIe / NVL / SXM (NVLink + SXM best for multi-GPU training)

If you want, I can also:

* Rank these GPUs by **LLM training suitability**
* Recommend **best RunPod GPU for 7B / 13B / 70B models**
* Convert this into **CSV / JSON**
* Map GPUs to **CUDA compute capability & tensor core generation**

Just tell me how you want to use this data.
