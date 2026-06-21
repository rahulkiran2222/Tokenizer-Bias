import math

def calculate_bpb(loss, total_bytes):
    """
    BPB = Total Loss (in nats) / (Total Bytes * log(2))
    """
    return loss / (math.log(2))
