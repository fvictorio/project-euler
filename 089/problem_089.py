import re

def roman_to_arabic(s):
    total = 0
    while s and s[0] == 'M':
        total += 1000
        s = s[1:]
    while s and s[0:2] == 'CM':
        total += 900
        s = s[2:]
    while s and s[0] == 'D':
        total += 500
        s = s[1:]
    while s and s[0:2] == 'CD':
        total += 400
        s = s[2:]
    while s and s[0] == 'C':
        total += 100
        s = s[1:]
    while s and s[0:2] == 'XC':
        total += 90
        s = s[2:]
    while s and s[0] == 'L':
        total += 50
        s = s[1:]
    while s and s[0:2] == 'XL':
        total += 40
        s = s[2:]
    while s and s[0] == 'X':
        total += 10
        s = s[1:]
    while s and s[0:2] == 'IX':
        total += 9
        s = s[2:]
    while s and s[0] == 'V':
        total += 5
        s = s[1:]
    while s and s[0:2] == 'IV':
        total += 4
        s = s[2:]
    while s and s[0] == 'I':
        total += 1
        s = s[1:]
    return total

def arabic_to_roman(i):
    result = ''
    while i > 0:
        if i >= 1000:
            result += 'M'
            i -= 1000
        elif i >= 900:
            result += 'CM'
            i -= 900
        elif i >= 500:
            result += 'D'
            i -= 500
        elif i >= 400:
            result += 'CD'
            i -= 400
        elif i >= 100:
            result += 'C'
            i -= 100
        elif i >= 90:
            result += 'XC'
            i -= 90
        elif i >= 50:
            result += 'L'
            i -= 50
        elif i >= 40:
            result += 'XL'
            i -= 40
        elif i >= 10:
            result += 'X'
            i -= 10
        elif i >= 9:
            result += 'IX'
            i -= 9
        elif i >= 5:
            result += 'V'
            i -= 5
        elif i >= 4:
            result += 'IV'
            i -= 4
        elif i >= 1:
            result += 'I'
            i -= 1
    return result

def minimal(s): # write the roman numeral s in minimal form
    return arabic_to_roman(roman_to_arabic(s))

# read roman numerals
numbers = []
for n in open('roman.txt').readlines():
    numbers.append(re.sub('[\r\n]', '', n))

total = 0
for n in numbers:
    total += len(n) - len(minimal(n))
print total
