import gradio as gr
import torch
from transformers import AutoTokenizer
from utils.robustness import get_ocr_noise, get_transliteration
from utils.metrics import get_fragmentation_stats

tokenizer = AutoTokenizer.from_pretrained("NousResearch/Llama-2-7b-hf")

def run_experiment(text):
    stats = get_fragmentation_stats(text, tokenizer)
    ocr = get_ocr_noise(text)
    trans = get_transliteration(text)
    
    return {
        "Llama Tokens": stats['llama_len'],
        "Byte Count": stats['byte_len'],
        "Fertility Ratio": round(stats['ratio'], 2),
        "OCR Output": ocr,
        "Transliterated": trans
    }

demo = gr.Interface(
    fn=run_experiment,
    inputs=gr.Textbox(lines=2, placeholder="Enter Hindi/Telugu text..."),
    outputs="json",
    title="Tokenizer Bias & Robustness Analyzer"
)

if __name__ == "__main__":
    demo.launch()
