import random
import string
import tkinter as tk
from tkinter import ttk

alpha = {
    'a': 'R', 'b': 'x', 'c': 'D', 'd': 'm', 'e': 'Q', 'f': 'k', 'g': 'e',
    'h': 'z', 'i': 'y', 'j': 'a', 'k': 'W', 'l': 'o', 'm': 'A', 'n': 'p',
    'o': 'b', 'p': 'u', 'q': 'f', 'r': 'V', 's': 'N', 't': 'H', 'u': 'J',
    'v': 'i', 'w': 'd', 'x': 'K', 'y': 'w', 'z': 'g',
    'A': 'T', 'B': 'O', 'C': 'G', 'D': 'B', 'E': 'I', 'F': 'X', 'G': 'F',
    'H': 'q', 'I': 'Y', 'J': 'S', 'K': 'U', 'L': 'v', 'M': 'n', 'N': 'j',
    'O': 'Z', 'P': 'M', 'Q': 'h', 'R': 'P', 'S': 'C', 'T': 'r', 'U': 's',
    'V': 'l', 'W': 'c', 'X': 'E', 'Y': 't', 'Z': 'L',
    '0': '8', '1': '3', '2': '9', '3': '2', '4': '7', '5': '5', '6': '4',
    '7': '6', '8': '0', '9': '1'
}


def encryption(msg_list):
    encr_msg = ""
    for char in msg_list:
        if char in alpha:
            encr_msg += alpha[char]
        else:
            encr_msg += char

    extra_str = list(encr_msg)
    i = 0
    while i < len(extra_str):
        for _ in range(5): 
            random_str = random.choice(string.ascii_letters + string.digits)
            extra_str.insert(i + 1, random_str)
            i += 1 
        i += 1
    
    return "".join(extra_str)

def decryption(encr_msg):
    
    reverse_alpha = {v: k for k, v in alpha.items()}
    
    filtered_msg = [char for i, char in enumerate(encr_msg) if (i % 6) == 0]
    
    dencr_msg = ""
    for char in filtered_msg:
        if char in reverse_alpha:
            dencr_msg += reverse_alpha[char]
        else:
            dencr_msg += char
    
    return dencr_msg

def on_encrypt():
    msg = input_entry.get()
    msg_list = list(msg)
    encrypted_msg = encryption(msg_list)
    output_entry.delete(0, tk.END)
    output_entry.insert(0, encrypted_msg)

def on_decrypt():
    encrypted_msg = input_entry.get()
    dencr_msg = decryption(encrypted_msg)
    output_entry.delete(0, tk.END)
    output_entry.insert(0, dencr_msg)


root = tk.Tk()
root.title("Gir Encryption or Decryption")


ttk.Label(root, text="Input Message:").grid(column=0, row=0, padx=10, pady=10)
input_entry = ttk.Entry(root, width=50)
input_entry.grid(column=1, row=0, padx=10, pady=10)

ttk.Label(root, text="Output Message:").grid(column=0, row=1, padx=10, pady=10)
output_entry = ttk.Entry(root, width=50)
output_entry.grid(column=1, row=1, padx=10, pady=10)

encrypt_button = ttk.Button(root, text="Encrypt", command=on_encrypt)
encrypt_button.grid(column=0, row=2, padx=10, pady=10)

decrypt_button = ttk.Button(root, text="Decrypt", command=on_decrypt)
decrypt_button.grid(column=1, row=2, padx=10, pady=10)


root.mainloop()
