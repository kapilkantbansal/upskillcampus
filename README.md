# Secure Vault - Python Password Manager

A CLI-based password manager that stores your credentials securely using real encryption.

## What I used and why

- **bcrypt** — to hash the master password (one-way, can't be reversed)
- **Argon2id** — to derive the encryption key from master password (memory-hard, makes brute force practically impossible)
- **AES-256-GCM** — to encrypt stored passwords (modern authenticated encryption)

The encryption key is never stored anywhere — it's derived fresh every session from your master password.

## Setup

```bash
pip install bcrypt argon2-cffi cryptography
python main.py
```

## How it works

First run asks you to set a master password. After that, every login derives the encryption key from that password and uses it to encrypt/decrypt your saved credentials.

## Note

`vault.json` is gitignored intentionally — it contains your encrypted credentials and should never be pushed to GitHub.
