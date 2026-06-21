from transformers import AutoTokenizer
import torch

def analyze_fragmentation(text_list, model_name="hf-internal-testing/llama-tokenizer"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    results = {
        "llama_tokens": [],
        "byte_tokens": [],
        "char_count": []
    }
    
    for text in text_list:
        # Llama Tokenization
        llama_ids = tokenizer.encode(text)
        # Byte Tokenization (UTF-8)
        byte_ids = list(text.encode('utf-8'))
        
        results["llama_tokens"].append(len(llama_ids))
        results["byte_tokens"].append(len(byte_ids))
        results["char_count"].append(len(text))
        
    return results

# Example Usage:
# texts = ["नमस्ते", "హలో"]
# print(analyze_fragmentation(texts))
