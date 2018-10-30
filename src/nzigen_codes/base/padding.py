
def unpad(code: str) -> str:
    pad = code[len(code) - 1]
    pad = pad if isinstance(pad, int) else ord(pad)
    if pad <= 0:
        raise ValueError('padding is zero')
    return code[:-pad]


def pad(string: str, block_size: int) -> str:
    padding = (block_size - len(string)) % block_size
    if padding == 0:
        padding = block_size
    return string + padding * chr(padding)
