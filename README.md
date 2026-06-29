# 🔤 Tokenizer-Bias

<div align="center">

### Understanding the *Indic Tax*: Byte-Level vs. Subword Representations

**Quantifying tokenization fragmentation • Measuring linguistic bias • Exploring tokenizer-free representations**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)]()
[![PyTorch](https://img.shields.io/badge/PyTorch-2.x-red.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()
[![Research](https://img.shields.io/badge/Research-NLP%20%7C%20Foundation%20Models-purple.svg)]()

### 🌐 Live Demo

**https://huggingface.co/spaces/RahulKiran2222/tokenizer-bias**

---

*Investigating tokenization inefficiency and robustness in Hindi and Telugu for next-generation foundation models.*

</div>

---

# Overview

**Tokenizer-Bias** is an experimental framework for studying the hidden costs introduced by modern subword tokenization in Indic languages.

While large language models are optimized primarily for English, morphologically rich and underrepresented languages often experience severe token fragmentation, resulting in:

* Increased token usage and computational overhead.
* Reduced effective context length.
* Vocabulary inefficiencies.
* Sensitivity to transliteration and OCR corruption.
* Poor robustness under multilingual and code-switched settings.

Inspired by recent tokenizer-free architectures such as **ByT5**, **CANINE**, **MegaByte**, **BLT**, and **MambaByte**, this project explores whether byte-level representations provide a more universal alternative.

---

# Research Questions

### RQ1 — Tokenization Bias

How much fragmentation do modern tokenizers introduce for Hindi and Telugu?

### RQ2 — Representation Efficiency

How do byte-level representations compare with subword tokenization?

### RQ3 — Robustness

How do both approaches behave under:

* Transliteration
* Code-switching
* OCR-induced perturbations

### RQ4 — Toward Tokenizer-Free Foundation Models

Can these observations motivate future multimodal tokenizer-free architectures?

---

# System Overview

```text
               Raw Text
                   │
        ┌──────────┴──────────┐
        │                     │
  Llama Tokenizer         UTF-8 Bytes
        │                     │
        ├──── Token Statistics
        ├──── Compression Analysis
        ├──── Sequence Inflation
        │
        └──────────────┐
                       │
              Tiny Language Models
                       │
            Robustness Evaluation
                       │
     Transliteration • OCR • Code-Switching
```

---

# Features

## Tokenization Analysis

Compare:

* Llama tokenizer
* GPT tokenizers
* UTF-8 byte representations

Metrics:

* Token count
* Sequence inflation
* Compression ratio
* Vocabulary utilization
* Token fertility

---

## Robustness Evaluation

Study model behavior under realistic perturbations:

### Transliteration

```text
namaste
↓
नमस्ते
```

### Code-Switching

```text
आज meeting cancel हो गयी।
```

### OCR Corruption

Real image-based OCR loop:

```text
Text
↓
Image Rendering
↓
Blur + Noise
↓
Tesseract OCR
↓
Recovered Text
↓
Character-Level Errors
```

---

## Tiny Language Model Experiments

Baseline:

```text
Llama Tokenizer
↓
TinyGPT
↓
Prediction
```

Tokenizer-Free:

```text
UTF-8 Bytes
↓
TinyGPT
↓
Prediction
```

Metrics:

* Loss
* Perplexity
* Bits-per-byte (BPB)
* Robustness degradation

---

# Datasets

### IndicCorp v2

Languages:

* Hindi
* Telugu

Reference Corpus:

* English subset from OSCAR

Split:

```text
Train      80%
Validation 10%
Test       10%
```

---

# Evaluation Metrics

| Category            | Metrics                      |
| ------------------- | ---------------------------- |
| Tokenization        | Token count, Fertility Ratio |
| Efficiency          | Compression Ratio            |
| Modeling            | Loss, Perplexity             |
| Byte-Level Modeling | Bits-per-Byte                |
| Robustness          | Accuracy degradation         |
| Error Analysis      | Character confusion matrices |

---

# Early Experiments (*Limitations Applicable)

Early experiments with the live demo show a consistent pattern: Hindi and Telugu text is
fragmented into substantially more subword tokens per character than comparable English
text under the Llama tokenizer, and the gap widens for Telugu, which is more
morphologically dense and less represented in the tokenizer's training data. This supports
the core hypothesis — that subword tokenizers impose an uneven computational and context-length
cost across languages — but exact numeric fertility ratios are still being validated
across tokenizer backends and are intentionally omitted here pending a more rigorous
benchmark pass (see Limitations).

---

# Repository Structure

```bash
tokenizer-bias/

├── data/
├── tokenizer_analysis/
│   ├── token_count.py
│   ├── compression_ratio.py
│   ├── sequence_inflation.py
│   └── vocab_fragmentation.py
│
├── encoders/
│   └── utf8_encoder.py
│
├── models/
│   ├── gpt_llama.py
│   └── gpt_byte.py
│
├── training/
│   ├── train_llama.py
│   └── train_byte.py
│
├── robustness/
│   ├── transliteration.py
│   ├── code_switching.py
│   ├── render_text.py
│   ├── add_noise.py
│   └── run_tesseract.py
│
├── evaluation/
├── analysis/
├── plots/
├── report/
└── README.md
```

---

# Installation

### Clone Repository

```bash
git clone https://github.com/rahulkiran2222/tokenizer-bias.git

cd tokenizer-bias
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Application

```bash
python app.py
```

---

# Limitations

* Tiny language models are intended for representation analysis rather than fluent generation.
* OCR evaluation depends on rendering quality and language-specific fonts.
* Experiments currently focus on Hindi and Telugu only.
* Results are not intended as large-scale benchmark conclusions.

---

# Future Directions

## Byte-Mamba

```text
Bytes
↓
Mamba
↓
Language Model
```

---

## Dynamic Byte Patching

Inspired by Meta's BLT:

```text
Bytes
↓
Dynamic Patches
↓
Latent Transformer
```

---

## Tokenizer-Free Multimodal Models

```text
Pixels + Bytes
↓
Shared Backbone
↓
Foundation Model
```

---

# Inspiration

This work is inspired by:

* ByT5
* CANINE
* MegaByte
* Byte Latent Transformer (BLT)
* MambaByte

and aligns with ongoing research in tokenizer-free language and vision foundation models.

---

# Citation

```bibtex
@software{tokenizer_bias_2026,
  author = {Rahul Kiran G},
  title = {Tokenizer-Bias: Understanding Byte-Level and Subword Representations},
  year = {2026},
  url = {https://github.com/rahulkiran2222/tokenizer-bias}
}
```
# LIMITATIONS
* Reported fertility ratios are sensitive to the specific tokenizer checkpoint and
  fast/slow tokenizer backend used; numeric results are being re-validated before
  being published in the README and will be added once confirmed.
  
---

# Author

### Rahul Kiran G

AI Researcher • Foundation Models • Multilingual NLP • Tokenizer-Free Architectures

> *Understanding language beyond tokens.*
