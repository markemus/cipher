# Cipher

Cipher lets you encrypt and decrypt messages using a primitive command line. It was my first serious attempt to parse user data to carry out functions.

# Directions

There are two built-in ciphers: atbash and caesar (Vigenere is also coded, but not implemented
for the command line). Both atbash and caesar ciphers can be easily decoded- atbash simply by
running the string through again, and caesar by reversing the shift.

The following codes are recognized:

Cipher names:
at_bash
caesar

Strings:
"string goes here"

Pipes:
|

Parameters (for caesar):
(5)

Example:
"helloworld" => helloworld
"helloworld" | at_bash => svooldliow
"helloworld" | at_bash | caesar (5) => xattqiqntb

# Installation

Install python3

# To Run

python3 main.py
