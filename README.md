Gir Encryption or Decryption Tool
This Python application provides a simple encryption and decryption tool using a custom substitution cipher and a graphical user interface built with Tkinter.

Features:
Encryption: Transforms a given input message into an encrypted format by substituting characters based on a predefined mapping and adding random characters for added complexity.
Decryption: Reverses the encryption process to retrieve the original message by filtering out the random characters and substituting back to the original characters.
Graphical User Interface (GUI): Easy-to-use interface to input the message, perform encryption or decryption, and view the results.
Dependencies:
Python 3.x
Tkinter (usually included with Python)
random (standard Python library)
string (standard Python library)
Code Description:
Character Mapping:

alpha: A dictionary mapping for substitution cipher used in encryption.
reverse_alpha: Automatically generated reverse mapping used in decryption.
Encryption:

encryption(msg_list): Encrypts the input message by substituting characters based on alpha and inserts random characters at regular intervals.
Decryption:

decryption(encr_msg): Decrypts the input message by filtering out the random characters and substituting back the original characters using reverse_alpha.
GUI Functions:

on_encrypt(): Retrieves input from the user, encrypts it, and displays the encrypted message.
on_decrypt(): Retrieves the encrypted message, decrypts it, and displays the original message.
GUI Setup:

Tkinter is used to create the graphical user interface.
Includes input and output fields, and buttons to trigger encryption and decryption.
How to Use:
Run the Script:

Execute the script to launch the GUI.
Encrypt a Message:

Enter your message in the "Input Message" field.
Click the "Encrypt" button to see the encrypted message in the "Output Message" field.
Decrypt a Message:

Enter the encrypted message in the "Input Message" field.
Click the "Decrypt" button to see the original message in the "Output Message" field.

Example Usage:
python gir_encryption_tool.py
