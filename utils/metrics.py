import math

def calculate_bpb(loss):
    return loss / math.log(2)

def get_fragmentation_stats(text, tokenizer):
    llama_tokens = tokenizer.encode(text)
    byte_tokens = list(text.encode('utf-8'))
    return {
        "char_len": len(text),
        "llama_len": len(llama_tokens),
        "byte_len": len(byte_tokens),
        "ratio": len(llama_tokens) / len(text.split()) if len(text.split()) > 0 else 0
    }
