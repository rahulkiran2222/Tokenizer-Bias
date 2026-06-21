📝 Tokenizer Bias: The "Indic Tax" in Foundation Models
![alt text](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Live%20Demo-blue)

![alt text](https://img.shields.io/badge/python-3.8+-green.svg)

![alt text](https://img.shields.io/badge/License-MIT-yellow.svg)

Understanding Byte-Level vs. Subword Representations in Hindi & Telugu
Modern AI models like Llama are primarily optimized for English. This project investigates the "Indic Tax"—the extreme fragmentation and inefficiency introduced by standard tokenizers when processing morphologically rich languages like Hindi and Telugu.

🚀 Live Demo
Try the interactive Tokenizer Bias Analyzer here:
👉 Hugging Face Space Link

🧐 The Problem: Tokenizer Fragmentation
When an English word like Hello is processed, it counts as 1 token. When the Telugu word నమస్కారం is processed by the Llama tokenizer, it is fragmented into 24 tokens.

This leads to:

Higher Costs: Users pay more for the same information.

Slow Inference: High token counts increase latency.

Robustness Issues: Small OCR errors or typos break subword patterns completely.

🔍 Research Questions
RQ1: How much fragmentation do modern tokenizers introduce for Hindi and Telugu?

RQ2: Do byte-level representations provide better vocabulary utilization?

RQ3: How robust are these models under transliteration, code-switching, and OCR-induced corruption?

RQ4: Can byte-level modeling motivate future tokenizer-free multimodal models?

🛠 Project Structure
code
Bash
tokenizer-bias/
├── core/               # TinyGPT Architecture & Streaming Datasets
├── utils/              # OCR Noise, Transliteration & BPB Metrics
├── app.py              # Gradio Interface for Live Demo
├── setup_env.sh        # System & Tesseract Setup
├── requirements.txt    # Python Dependencies
└── packages.txt        # Hugging Face Space System Dependencies
📊 Key Findings (Experimental Results)
Metric	English	Hindi	Telugu
Tokens per Word (Llama)	~1.1	~4.5	~10+
Byte vs. Token Ratio	1:1	1:3	1:1 (Max Fragmentation)
Robustness (OCR)	High	Medium	Low
Observation: Our analysis shows that for Telugu, subword tokenizers like Llama's provide zero compression, essentially falling back to byte-level processing but with the overhead of a 32,000+ entry vocabulary.
📦 Installation & Setup

Local Setup
Clone the repo:

code
Bash
git clone https://github.com/rahulkiran2222/tokenizer-bias.git
cd tokenizer-bias
Install system dependencies (Tesseract):

code
Bash
bash setup_env.sh
Run the Live Demo:

code
Bash
python app.py
Running on Google Colab / Kaggle
Simply open the notebooks/experiment_demo.ipynb and run all cells to train the TinyGPT models (5M-20M parameters) on IndicCorp v2 data.

🧪 Robustness Analysis
This project includes a custom pipeline to simulate real-world errors:

OCR-Induced Corruption: Renders text to images, adds Gaussian noise/blur, and recovers it via Tesseract to study character confusion.

Transliteration: Converts native scripts to Latin (e.g., नमस्ते → namaste) to test cross-script understanding.

🔮 Future Directions

V2: Expansion to Tamil and Kannada.

V3: Implementation of BLT (Byte Latent Transformer) for dynamic patching.

V4: Byte-Mamba integration for long-context Indic processing.
🤝 Acknowledgments
Datasets: IndicCorp v2 / OSCAR

Inspiration: Inspired by the work of Yuki Asano and the MegaByte research team on tokenizer-free modeling.

Created as part of an investigation into Linguistic Bias in Foundation Models.
