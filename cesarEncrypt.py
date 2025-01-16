#!/usr/bin/env python
# -*- coding: utf-8 -*

letter_frequencies = {
    'E': 17.35,
    'A': 8.20,
    'S': 7.93,
    'I': 7.53,
    'N': 7.17,
    'T': 6.99,
    'R': 6.65,
    'L': 5.92,
    'U': 5.73,
    'O': 5.53,
    'D': 4.01,
    'C': 3.33,
    'M': 2.97,
    'P': 2.92,
    'V': 1.39,
    'G': 1.09,
    'F': 1.08,
    'Q': 1.04,
    'H': 0.93,
    'B': 0.92,
    'X': 0.47,
    'J': 0.34,
    'Y': 0.31,
    'Z': 0.10,
    'K': 0.06,
    'W': 0.03
}

# for letter, frequency in letter_frequencies.items():
#     print(f"Lettre : {letter}, Fréquence : {frequency}%")

def cesar(sentence , number):

    encryprtSentence = ''

    for L in sentence:
        if L == ' ':
            encryprtSentence += ' '
        else:
            indexOfL = ord(L)
            indexLenght = indexOfL + number
            if indexLenght > 122:
                indexLenght -= 26
            encryprtSentence += chr(indexLenght)
    return encryprtSentence

def cesardecode(sentence):
    tableFrequence = {}
    for L in sentence:
        if L.isalpha():
            L = L.upper()
            if L in tableFrequence:
                tableFrequence[L] += 1
            else:
                tableFrequence[L] = 1

    total_letters = sum(tableFrequence.values())

    for letter , freq in tableFrequence.items():
        frequency = (freq / total_letters) * 100
        frequencyWaited = letter_frequencies.get(letter)
        freqTest = (frequency - frequencyWaited)/ frequencyWaited
        print(f"{letter} : {frequency} , {frequencyWaited}")
        print(freqTest)


if __name__ == '__main__':

    sentence = (input("quel est votre phrase a encrypter ? : "))
    numberEncrypt = int((input("choisir un nombre d'encryption : ")))

    print(cesar(sentence , numberEncrypt))
    sentence = cesar(sentence , numberEncrypt)
    cesardecode(sentence)