
def unpad(code) -> bytes:
    binary = bytes(code, 'utf-8') if isinstance(code, str) else code
    pad = code[len(binary) - 1]
    pad = pad if isinstance(pad, int) else ord(pad)
    if pad <= 0:
        raise ValueError('padding is zero')
    return binary[:-pad]


def pad(string, block_size: int) -> bytes:
    binary = bytes(string, 'utf-8') if isinstance(string, str) else string
    padding = (block_size - len(binary)) % block_size
    if padding == 0:
        padding = block_size
    return binary + padding * bytes(chr(padding), 'utf-8')
