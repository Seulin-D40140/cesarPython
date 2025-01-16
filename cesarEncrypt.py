#!/usr/bin/env python
# -*- coding: utf-8 -*


def cesar(sentence , number):
    """

    :param sentence:
    :param number:
    :return: string
    """
    # alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    encryprtSentence = ''

    # for L in sentence:
    #     try:
    #         indexOfL = alphabet.index(L)
    #
    #         indexTest = indexOfL + number
    #         if indexTest > len(alphabet) -1:
    #             lenght = indexTest - (len(alphabet) -1)
    #             indexTest = lenght
    #         encryprtSentence += alphabet[indexTest]
    #     except ValueError :
    #         encryprtSentence += '!'

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


if __name__ == '__main__':

    sentence = (input("quel est votre phrase a encrypter ? : "))
    numberEncrypt = int((input("choisir un nombre d'encryption : ")))

    print(cesar(sentence , numberEncrypt))