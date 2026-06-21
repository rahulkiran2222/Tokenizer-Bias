🔤 Tokenizer-Bias

Understanding the "Indic Tax": Byte-Level vs. Subword Representations
Quantifying tokenizer fragmentation. Measuring linguistic bias. Building robust byte-level alternatives.
🌐 Live Demo: https://huggingface.co/spaces/RahulKiran2222/tokenizer-bias
⚡ Research Focus: Inefficiency in Hindi & Telugu LLM Processing

🧠 Overview
IndicToken-Bias is a research framework and analytics platform designed to expose the hidden "tax" paid by Indic languages in modern AI. While English tokenization is highly efficient, languages like Hindi and Telugu suffer from extreme fragmentation, leading to:

Inflated Costs: 3–10x more tokens for the same semantic meaning.

Performance Degradation: Narrower context windows for non-English users.

Robustness Failures: Brittleness under OCR noise and transliteration.

✨ Features

⚔️ Fragmentation Battle
Compare standard tokenizers (Llama/GPT) vs. Raw UTF-8 Bytes:

Token Inflation: Visualize how one word becomes 20+ tokens 📈

Compression Ratios: Bytes per token efficiency tracking 📉

Vocabulary Heatmaps: Identifying "dead" areas in large vocabularies.

🛡️ Robustness Stress-Test
Analyze how models handle real-world "dirty" data:

OCR Noise Sim: Real-time rendering and recovery using Tesseract.

Transliteration: Cross-script analysis (e.g., Devanagari ↔ Latin).

Code-Switching: Handling Hinglish/Teluglish transitions.

🌱 TinyGPT Laboratory
Byte-Level Modeling: Train 5M–20M parameter models directly on bytes.

BPB Metric: Standardized "Bits-Per-Byte" evaluation for fair comparison.

Latent Analysis: Visualize character confusion matrices.

🎨 Research UI
Live Analyzer: Real-time tokenization feedback for Hindi/Telugu.

Fragmentation Scores: Instant "Indic Tax" calculation.

Modern Design: Clean, interactive interface for researcher exploration.

🧪 How It Works

The Fragmentation Metric
Calculates the Fertility Ratio: 
R
=
N
t
o
k
e
n
s
N
w
o
r
d
s
R= 
N 
words
​	
 
N 
tokens
​	
 
​	
 

Compares Llama's subword efficiency against raw UTF-8 byte distribution.

OCR Corruption Pipeline
Render: Text converted to 300 DPI images.

Distort: Gaussian blur, salt-and-pepper noise, and rotation applied.

Recover: Tesseract OCR attempts to rebuild text to identify character-level vulnerability.

Evaluation Engine
Uses Bits-Per-Byte (BPB) to normalize performance between models with different vocabulary sizes (e.g., 256 for Bytes vs. 32,000 for Llama).

🛠️ Tech Stack

Backend & AI
Python 3.10+

PyTorch: Custom TinyGPT architecture.

Transformers/Tokenizers: Llama/Tiktoken integration.

Datasets: IndicCorp v2 / OSCAR streaming.

Robustness Tools
Pytesseract: Optical Character Recognition.

Pillow: Image-based noise simulation.

Indic-Transliteration: Script conversion engine.

Frontend & Live Demo
Gradio: Interactive web interface.

Hugging Face Spaces: Cloud hosting.

📊 Sample Research Results
Language	Llama Tokens (Word: "Hello")	Byte Count	Fertility Ratio
English	1	5	1.0x
Hindi	5	15	4.8x
Telugu	24	24	24.0x
🚀 Local Setup

1. Clone the repo
code
Bash
git clone https://github.com/rahulkiran2222/tokenizer-bias
cd tokenizer-bias
2. Environment Setup
code
Bash
# Setup system dependencies (OCR & Fonts)
bash setup_env.sh

# Install Python packages
pip install -r requirements.txt
3. Launch the Demo
code
Bash
python app.py
⚠️ Limitations
Model Scale: TinyGPT (20M) is for representation analysis, not fluent generation.

OCR Speed: Image rendering adds latency to the live demo.

Font Support: Requires fonts-indic for proper rendering in Linux environments.

🔮 Future Work
Byte-Mamba: Testing State-Space Models for long-sequence byte modeling.

Dynamic Patching: Investigating BLT (Byte Latent Transformer) for Indic scripts.

V5 Multimodal: Pixel-to-Byte shared backbone for tokenizer-free foundation models.

📚 Inspiration
Yuki Asano: Vision-language representation research.

MegaByte/ByT5: Tokenizer-free modeling architectures.

📜 License
MIT License

👤 Author
Rahul Kiran G
AI Researcher & Develope
