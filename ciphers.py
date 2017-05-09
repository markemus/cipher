

#inverse: run through again (involution)
def at_bash(statement):

    trans = {
    "a" : "z",
    "b" : "y",
    "c" : "x",
    "d" : "w",
    "e" : "v",
    "f" : "u",
    "g" : "t",
    "h" : "s",
    "i" : "r",
    "j" : "q",
    "k" : "p",
    "l" : "o",
    "m" : "n",
    "n" : "m",
    "o" : "l",
    "p" : "k",
    "q" : "j",
    "r" : "i",
    "s" : "h",
    "t" : "g",
    "u" : "f",
    "v" : "e",
    "w" : "d",
    "x" : "c",
    "y" : "b",
    "z" : "a"
    }

    out = ""

    for char in statement:
        out += trans[char.lower()]

    return out

#inverse: shift = -original shift
def caesar(statement, shift):

    all_char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    out = ""

    for char in statement:
        out += all_char[(all_char.index(char.lower()) + shift) % 26]

    return out

#to decrypt: compare encrypted char to key- plaintext char is table's column name for encrypted char in key's row. Should be simple algebraically.
def vigenere(statement, keyword):

    all_char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    vig_square = [[all_char[(all_char.index(in_char) + all_char.index(out_char)) % 26] for in_char in all_char] for out_char in all_char]

    while len(statement) > len(keyword):
        keyword = keyword + keyword

    keyword = keyword[:len(statement)]

    print(keyword)
    print(vig_square)

    out = ""

    for i in range(len(statement)):
        out += vig_square[all_char.index(statement[i])][all_char.index(keyword[i])]

    return(out)

print(vigenere("attackatdawn", "lemon"))