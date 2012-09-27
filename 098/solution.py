from math import sqrt
from itertools import permutations, combinations

test = not True
EPSILON = 10**-5
digits = range(10)

def is_square(n):
    return abs(n - round(sqrt(n))**2) < EPSILON

def is_anagram(w1, w2):
    return sorted(w1) == sorted(w2)

def value(w, p, letters):
    v = {}
    for i in range(len(p)):
        v[letters[i]] = p[i]
    return ''.join(str(v[i]) for i in w)

def is_square_anagram(w1, w2):
    values = []
    if not is_anagram(w1, w2): return -1
    letters = list(set(w1))
    length = len(letters)

    for p in permutations(digits, length):
        val_w1 = value(w1, p, letters)
        if val_w1[0] == '0': continue
        val_w1 = int(val_w1)
        if not is_square(val_w1): continue
        val_w2 = value(w2, p, letters)
        if val_w2[0] == '0': continue
        val_w2 = int(val_w2)
        if not is_square(val_w2): continue
        values.append(max(val_w1, val_w2))
    if not values: return -1
    return max(values)

if not test:
    #words = [i[1:-1] for i in open("words.txt").readlines()[0].split(',')]
    #anagrams = []

    #i = 0
    #while i < len(words):
    #    j = i + 1
    #    found_anagrams = False
    #    while j < len(words):
    #        if is_anagram(words[i], words[j]):
    #            if not found_anagrams:
    #                anagrams.append([words[j]])
    #                found_anagrams = True
    #            else:
    #                anagrams[-1].append(words[j])
    #            words.remove(words[j])
    #        else:
    #            j += 1
    #    if found_anagrams:
    #        anagrams[-1].append(words[i])
    #        words.remove(words[i])
    #    else:
    #        i += 1

    for anagram in anagrams:
        for w1, w2 in combinations(anagram, 2):
            result = is_square_anagram(w1, w2)
            if result != -1:
                print("%s and %s are square anagrams with %i" % (w1, w2, result))
