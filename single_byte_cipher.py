import sys
from tools import english_letter_frequency

arg = sys.argv 

if len(arg) != 2 : 
    exit() 


def alpha_cout (txt) : 
    count = 0
    for i  in txt: 
        if i.isalpha() : 
            count += 1
    return count


def xor(str, key) : 
    output = ""
    for i in str : 
        output += chr(ord(i) ^ key)
    return output

def getscore(txt) : 
    score = 0 
    alpha = 0 
    lentgh = alpha_cout(txt)
    letter_counts = {letter: 0 for letter in 'abcdefghijklmnopqrstuvwxyz'}
    for char in txt : 
        if char.isalpha() and char.lower() >= 'a' and char.lower() <= 'z' :
            alpha += 1 
            letter_counts[char.lower()] += 1
    if(lentgh):
        alpha =alpha * 100 / lentgh
    if (alpha > 80) : 
        for lettre in letter_counts :
            letter_counts[lettre] *=  100 / lentgh
            if (letter_counts[lettre] > english_letter_frequency[lettre] - 2)  and (letter_counts[lettre] < english_letter_frequency[lettre] + 2) : 
                score += 1
            if (letter_counts[lettre] > english_letter_frequency[lettre] - 1)  and (letter_counts[lettre] < english_letter_frequency[lettre] + 1) :
                score += 1 
    return score 


def get_key(cipher):
    score = 0
    k = 0
    plaintxt = ""
    for key in range(128):
        txt = xor(cipher, key)
        if score < getscore(txt): 
            plaintxt = txt
            score = getscore(txt)
            k = key
    return k,plaintxt

with open(arg[1],'r') as file :
    output = ""
    score = 0 
    while(content := file.readline()):
        key,txt = get_key(content)
        var = getscore(txt) 
        print(var)
        if(score < var):
            output = txt
            score = var
    print(output)
# cphr = xor(arg[1], 6)
# k = get_key(cphr)
# print(k)