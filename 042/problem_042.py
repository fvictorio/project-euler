def letter_value (l):
    return ord(l) - ord('A') + 1

def word_value (w):
    return sum(map(letter_value,w))
