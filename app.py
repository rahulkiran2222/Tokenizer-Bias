import gradio as gr
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")

def analyze(english_text, hindi_text):
    en_tokens = tokenizer.encode(english_text)
    hi_tokens = tokenizer.encode(hindi_text)
    
    tax = (len(hi_tokens) / len(en_tokens)) if len(en_tokens) > 0 else 0
    
    res = f"""
    ### Analysis:
    - **English Tokens:** {len(en_tokens)}
    - **Hindi Tokens:** {len(hi_tokens)}
    - **The 'Language Tax':** {tax:.2f}x (Hindi is {tax:.2f} times more expensive to process)
    """
    return res

demo = gr.Interface(
    fn=analyze,
    inputs=["text", "text"],
    outputs="markdown",
    title="Indic Tokenizer Bias Checker",
    description="Compare how Llama-2 tokenizes English vs Hindi."
)

demo.launch()
