import torch
from datasets import load_dataset
from transformers import AutoTokenizer

class TokenizerDataset(torch.utils.data.IterableDataset):
    def __init__(self, lang='hi', mode='byte', block_size=128):
        self.data = load_dataset("oscar", f"unshuffled_deduplicated_{lang}", split='train', streaming=True)
        self.mode = mode
        self.block_size = block_size
        if mode == 'llama':
            self.tokenizer = AutoTokenizer.from_pretrained("hf-internal-testing/llama-tokenizer")

    def __iter__(self):
        for item in self.data:
            text = item['text']
            tokens = list(text.encode('utf-8')) if self.mode == 'byte' else self.tokenizer.encode(text)
            for i in range(0, len(tokens) - self.block_size, self.block_size):
                chunk = tokens[i:i + self.block_size + 1]
                yield torch.tensor(chunk[:-1]), torch.tensor(chunk[1:])
