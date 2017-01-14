import os
from time import sleep
import math

def read_file():

    file = open('text.txt', 'r')

    charList=list(file.read())

    return charList


def main():

    read_file()

    







if __name__ == "__main__":
    main()