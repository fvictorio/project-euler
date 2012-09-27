from string import ascii_lowercase

def decode (key, encoded):
    result = ''
    for i, c in enumerate(encoded):
        result += chr(c ^ ord(key[(i%len(key))]))
    return result

keys = []

if 1:
    for a in ascii_lowercase:
        for b in ascii_lowercase:
            for c in ascii_lowercase:
                key = a+b+c
                decoded = decode(key,encoded)
                if decoded.count('the') > 1:
                    keys.append(key)
