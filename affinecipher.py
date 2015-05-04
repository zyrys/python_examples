import sys
import cryptomath
import random
SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""


def main():

    mymessage = """"A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." -Alan Turing"""
    mykey = getrandomkey()nn
    mymode = 'encrypt'

    if mymode == 'encrypt':
        translated = encryptmessage(mykey, mymessage)
    elif mymode == 'decrypt':
        translated = decryptmessage(mykey, mymessage)
    print 'key %s' % mykey
    print '%sed text: ' %mymode.title()
    print translated


def getkeypart(key):

    keya = key // len(SYMBOLS)
    print keya
    keyb = key % len(SYMBOLS)
    print keyb
    return (keya, keyb)


def checkkeys(keya, keyb, mode):

    if keya == 1 and mode == 'encrypt':
        sys.exit('the affine cipher becomes incredibly weak when kay A is 1, Choose other key')
    if keyb == 0 and mode == 'decrypt':
        sys.exit('the affine cipher becomes wake when key B is 0, choose others')
    if keya < 0 or keyb < 0 or keyb > len(SYMBOLS) - 1:
        sys.exit('key A mus be greater than 0 and B between 0 and %s' % len(SYMBOLS) - 1)
    if cryptomath.gcd(keya, len(SYMBOLS)) != 1:
        sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (keya, len(SYMBOLS)))


def encryptmessage(key, message):
    keyA, keyB = getkeypart(key)
    checkkeys(keyA, keyB, 'encrypt')
    ciphertext = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            ciphertext += symbol
    return ciphertext


def decryptmessage(key, message):
    keyA, keyB = getkeypart(key)
    checkkeys(keyA, keyB, 'decrypt')
    plaintext = ''
    modInverseOfKeyA = cryptomath.findModInverse(keyA, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            symIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
        else:
            plaintext += symbol
    return plaintext


def getrandomkey():
    while True:
        keya = random.randint(2, len(SYMBOLS))
        keyb = random.randint(2, len(SYMBOLS))
        if cryptomath.gcd(keya, len(SYMBOLS)) == 1:
            return keya * len(SYMBOLS) + keyb

if __name__ == '__main__':
    main()