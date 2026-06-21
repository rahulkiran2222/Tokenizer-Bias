import torch
import torch.nn as nn
from torch.nn import functional as F

# Hyperparameters for 5M model
batch_size = 32
block_size = 256 # Context length
n_embd = 192
n_head = 6
n_layer = 6

class TinyGPT(nn.Module):
    def __init__(self, vocab_size):
        super().__init__()
        self.token_embedding_table = nn.Embedding(vocab_size, n_embd)
        self.position_embedding_table = nn.Embedding(block_size, n_embd)
        # Add Transformer Blocks here...
        self.lm_head = nn.Linear(n_embd, vocab_size)

    def forward(self, idx, targets=None):
        # standard GPT forward pass
        pass

# TRAINING STRATEGY:
# Train Model A: ByteTokenizer (vocab_size=256)
# Train Model B: LlamaTokenizer (vocab_size=32000)
