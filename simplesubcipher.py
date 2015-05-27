__author__ = 'zbyszek'

import sys
import random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    myMessage = 'If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of myths is explained in this way. -Bertrand Russell'
    #myMessage = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm'
    myKey = getrandomkey()
    mymode = 'encrypt'

    checkValidKey(myKey)

    if mymode == 'encrypt':
        translated = encryptmessage(myKey, myMessage)
    elif mymode == 'decrypt':
        translated = decryptmessage(myKey, myMessage)

    print 'Using key %s' %myKey
    print 'The %sed message is: ' %mymode
    print translated


def checkValidKey(key):
    keylist = list(key)
    letterslist = list(LETTERS)
    keylist.sort()
    letterslist.sort()
    if keylist != letterslist:
        sys.exit('There is an error in the key or symbol set')


def encryptmessage(key, message):
    return translatedmessage(key, message, 'encrypt')


def decryptmessage(key, message):
    return translatedmessage(key, message, 'decrypt')


def translatedmessage(key, message, mode):
    translated = ''
    charsa = LETTERS
    charsb = key
    if mode == 'decrypt':
        charsa, charsb = charsb, charsa

    for symbol in message:
        if symbol.upper() in charsa:
            symindex = charsa.find(symbol.upper())
            if symbol.isupper():
                translated += charsb[symindex].upper()
            else:
                translated += charsb[symindex].lower()
        else:
            translated += symbol

    return translated


def getrandomkey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


if __name__ == '__main__':
    main()
