import sys
from tools import english_letter_frequency

arg = sys.argv 

if len(arg) != 2 : 
    exit() 


str = arg[1]

def xor(str, key) : 
    output = ""
    for i in str : 
        output += chr(ord(i) ^ key)
    return output

def getscore(txt) : 
    score = 0 
    alpha = 0 
    letter_counts = {letter: 0 for letter in 'abcdefghijklmnopqrstuvwxyz'}
    for char in txt : 
        if char.isalpha():
            alpha += 1 
            char = char.lower()
            letter_counts[char] += 1
    alpha *= 100 / len(txt)
    if (alpha > 80) : 
        for lettre in letter_counts :
            letter_counts[lettre] *=  100 / len(txt)
            if (letter_counts[lettre] > english_letter_frequency[lettre] - 2)  and (letter_counts[lettre] < english_letter_frequency[lettre] + 2) : 
                score += 1
            if (letter_counts[lettre] > english_letter_frequency[lettre] - 1)  and (letter_counts[lettre] < english_letter_frequency[lettre] + 1) :
                score += 1 
    return score 


def get_key(txt):
    score = 0
    k = 0
    for key in range(128):
        txt = xor(str, key)
        if score < getscore(txt): 
            plaintxt = txt
            score = getscore(txt)
            k = key
    print(plaintxt)

get_key(xor(str, i))
