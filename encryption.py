import os
import base64
from argon2.low_level import hash_secret_raw, Type
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def generate_salt():
    return os.urandom(16)


def derive_key(master_password, salt):

    key = hash_secret_raw(
        secret=master_password.encode(),
        salt=salt,
        time_cost=3,
        memory_cost=65536,
        parallelism=4,
        hash_len=32,
        type=Type.ID
    )
    return key


def encrypt_password(website_password, key):

    password_bytes = website_password.encode()

    nonce = os.urandom(12)

    aesgcm = AESGCM(key)

    encrypted_bytes = aesgcm.encrypt(
        nonce,
        password_bytes,
        None
    )
    return base64.b64encode(nonce+encrypted_bytes).decode()


def decrypt_password(stored_string, key):
    raw = base64.b64decode(stored_string)
    nonce = raw[:12]       # pehle 12 bytes = nonce
    ciphertext = raw[12:]  # baaki sab = ciphertext
    aesgcm = AESGCM(key)

    decrypted_bytes = aesgcm.decrypt(
        nonce,
        ciphertext,
        None
    )
    return decrypted_bytes.decode()
