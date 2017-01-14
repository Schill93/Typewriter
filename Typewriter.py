import os
from time import sleep
import math
import string

def read_file():

    file = open('text.txt', 'r')

    charList=list(file.read())

    return charList


def printChar(letterIn):
    letters=string.ascii_lowercase+'åäö'
    Special=''
    numbers='1234567890'

    code_numbers=['110100','111111','111010','111011',' 110101','110110', '111100','110010','111000','110111','111101','110011','111001','110000']

    code_letters=['010011','100000','100011','100111','101100','001011','001111','100100','010010','001110','100010','100101','011111','101010','010101','000110','000010','010111','010100','100001','101011','011011','010000','101111','000100','010001','110001','000101','010110','001010']


    if letterIn.lower() in letters and letterIn.isupper():

        print('Versal')
    elif letterIn.lower() in letters:
        print('Gemener')
    elif letterIn in numbers:
        print('Number')
    elif letterIn in Special:
        print('Special')
    else:
        print('Not valid')



def main():

    charList=read_file()

    printChar('#')



if __name__ == "__main__":
    main()