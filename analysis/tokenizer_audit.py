import pandas as pd
from transformers import AutoTokenizer
from datasets import load_dataset
import matplotlib.pyplot as plt

def run_audit():
    # 1. Load Tokenizer & Parallel Data
    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")
    langs = {"eng_Latn": "English", "hin_Deva": "Hindi", "tel_Telu": "Telugu"}
    
    # Load 500 samples of parallel data
    dataset = load_dataset("facebook/flores", "all", split='dev', trust_remote_code=True)
    
    stats = []
    for lang_code, lang_name in langs.items():
        sentences = dataset[lang_code][:500]
        
        for text in sentences:
            tokens = tokenizer.encode(text, add_special_tokens=False)
            bytes_count = len(text.encode('utf-8'))
            
            stats.append({
                "Language": lang_name,
                "Tokens": len(tokens),
                "Bytes": bytes_count,
                "Fertility": len(tokens) / len(text.split()) if len(text.split()) > 0 else 0
            })
    
    df = pd.DataFrame(stats)
    
    # 2. Generate Results
    summary = df.groupby("Language").mean()
    print("\n--- TOKENIZER BIAS REPORT ---")
    print(summary)
    
    # 3. Save a plot
    df.groupby("Language")["Tokens"].mean().plot(kind='bar', title="Avg Tokens for Same Meaning")
    plt.ylabel("Sequence Length")
    plt.savefig("bias_chart.png")

if __name__ == "__main__":
    run_audit()
