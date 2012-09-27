import re

def count(word):
    return len(re.sub('[ \-]','',word))

def int_to_word (n):
    word = ""
    if n == 1:
        word = "one"
    elif n == 2:
        word = "two"
    elif n == 3:
        word = "three"
    elif n == 4:
        word = "four"
    elif n == 5:
        word = "five"
    elif n == 6:
        word = "six"
    elif n == 7:
        word = "seven"
    elif n == 8:
        word = "eight"
    elif n == 9:
        word = "nine"
    elif n == 10:
        word = "ten"
    elif n == 11:
        word = "eleven"
    elif n == 12:
        word = "twelve"
    elif n == 13:
        word = "thirteen"
    elif n == 14:
        word = "fourteen"
    elif n == 15:
        word = "fifteen"
    elif n == 16:
        word = "sixteen"
    elif n == 17:
        word = "seventeen"
    elif n == 18:
        word = "eighteen"
    elif n == 19:
        word = "nineteen"
    elif 20 <= n < 100:
        tens = n / 10
        if tens == 2:
            word = "twenty"
        elif tens == 3:
            word = "thirty"
        elif tens == 4:
            word = "forty"
        elif tens == 5:
            word = "fifty"
        elif tens == 6:
            word = "sixty"
        elif tens == 7:
            word = "seventy"
        elif tens == 8:
            word = "eighty"
        elif tens == 9:
            word = "ninety"
        if n % 10 != 0:
            word += ("-" + int_to_word(n % 10))
    elif 100 <= n < 1000:
        hundreds = n / 100
        if hundreds == 1:
            word = "one hundred"
        elif hundreds == 2:
            word = "two hundred"
        elif hundreds == 3:
            word = "three hundred"
        elif hundreds == 4:
            word = "four hundred"
        elif hundreds == 5:
            word = "five hundred"
        elif hundreds == 6:
            word = "six hundred"
        elif hundreds == 7:
            word = "seven hundred"
        elif hundreds == 8:
            word = "eight hundred"
        elif hundreds == 9:
            word = "nine hundred"
        if n % 100 != 0:
            word += (" and " + int_to_word(n % 100))
    return word
