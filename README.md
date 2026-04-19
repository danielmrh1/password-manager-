# Secure Password Manager

A simple CLI tool to store and manage passwords locally. I built this to understand how to implement basic encryption in Python and how to handle local data storage securely.

## Why I built this
Storing passwords in plain text files is a major security risk. This project uses the `cryptography` library to ensure that even if the storage file is accessed, the data remains unreadable without the correct key.

## Main Features
* **AES Encryption:** Uses the Fernet (Symmetric encryption) standard.
* **Local Storage:** All data is saved in a local `passwords.txt` file.
* **Key Management:** Automatically generates a `secret.key` on the first run.

## How it works
The program encrypts your password before writing it to the disk. When you want to view your passwords, it reads the encrypted string and uses your local key to decrypt it back into plain text.

[attachment_0](attachment)

## Usage
1.  **Install dependencies:**
    pip install cryptography

2.  **Run the script:**
    python src/pm.py

3.  **Choose mode:**
    - Type `add` to save a new password.
    - Type `view` to see your saved credentials.

## Important Note
The `secret.key` file is crucial. If you delete it, you will lose access to all your saved passwords as they cannot be decrypted without it. I've added this file to `.gitignore` to prevent uploading it to GitHub for security reasons.

## Author
Daniel Mrh
