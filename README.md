# BlockchainCryptography
This repo is all about how blockachain uses cryptography for transactions and trying to emulate it using python code


## When correct message was entered for verification :
![image](https://user-images.githubusercontent.com/76248886/209544883-7f19b532-99f4-4680-869b-55be763126f2.png)

## When incorrect message was entered for verification :
![image](https://user-images.githubusercontent.com/76248886/209545001-967e51c0-14d1-49f0-a851-ef01b8400a9d.png)

# Code Explanation:
This code is implementing a basic digital signature system using the Python cryptography library.

A digital signature is a way to ensure the authenticity and integrity of a message or document. It allows the recipient of a message to verify that the message was actually sent by the claimed sender and that the message has not been tampered with during transmission.

The code first imports several functions and classes from the cryptography library that are needed for digital signature.

The gneratekeys function generates a pair of private and public keys using the RSA algorithm. The private key is used to create a digital signature, and the public key is used to verify the signature.

The sign function takes a message and a private key as input, and returns a digital signature for the message. It first encodes the message as bytes using the UTF-8 encoding, and then uses the sign method of the private key to create the signature.

The verify function takes a signature, a message, and a public key as input, and verifies that the signature is valid for the message. It first encodes the message as bytes using the UTF-8 encoding, and then uses the verify method of the public key to check the signature. If the signature is valid, it prints a message saying that the message is verified. If the signature is invalid, it prints a message saying that the message does not match.

Finally, the code calls the gneratekeys, sign, and verify functions to demonstrate how the digital signature system works. It generates a pair of keys, creates a signature for a message using the private key, and then verifies the signature using the public key. It also tries to verify the signature for an incorrect message, which should fail.
