"""
--------------------------------------------------
SIMPLE MESSAGE ENCRYPTION & DECRYPTION
--------------------------------------------------

This script demonstrates a simple substitution cipher:
- Each character (letters, digits, punctuation, space) is replaced with a shuffled character.
- Encryption maps plain text → cipher text
- Decryption maps cipher text → original plain text
--------------------------------------------------
"""

import random
import string

# -----------------------------------------
# Step 1: Prepare characters and keys
# -----------------------------------------
# All possible characters to encode
chars = " " + string.punctuation + string.digits + string.ascii_letters

# Convert string to list for easy indexing
chars = list(chars)

# Create a copy for the key mapping and shuffle it
keys = chars.copy()
random.shuffle(keys)  # random substitution

# -----------------------------------------
# Step 2: Encrypt a message
# -----------------------------------------
plain_text = input("Enter message to encrypt: ")
cipher_text = ""  # Empty string to store encrypted message

for ch in plain_text:
    # Find index of character in original list
    index = chars.index(ch)
    # Replace with the character at same index in shuffled keys
    cipher_text += keys[index]

print(f"Encrypted message: {cipher_text}")

# -----------------------------------------
# Step 3: Decrypt a message
# -----------------------------------------
encrypted_text = input("Enter message to decrypt: ")
decrypted_text = ""

for ch in encrypted_text:
    # Find index of character in keys list
    index = keys.index(ch)
    # Replace with original character from chars
    decrypted_text += chars[index]

print(f"Decrypted message: {decrypted_text}")