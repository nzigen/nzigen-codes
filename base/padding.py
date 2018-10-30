
def pad(string: str, block_size: int) -> str:
    padding = (block_size - len(string)) % block_size
    if padding == 0:
        padding = block_size
    return string + padding * chr(padding)


def unpad(code: str) -> str:
    pad = ord(code[len(code) - 1])
    if pad <= 0:
        raise ValueError('padding is zero')
    return code[:-pad]
