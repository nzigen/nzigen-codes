from base64 import b64decode, b64encode

from Crypto import Random
from Crypto.Cipher import AES

from base.padding import unpad, pad


def decrypt_text(key, encrypted):
    try:
        code = b64decode(encrypted)
        iv = code[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(code[AES.block_size:]))
    except TypeError:
        return None


def encrypt_text(key, plaintext):
    plaintext = pad(plaintext, AES.block_size)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return b64encode(iv + cipher.encrypt(plaintext))
