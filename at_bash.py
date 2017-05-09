

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
        out += trans[char]

    return out

def caesar(statement, shift):

    all_char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]