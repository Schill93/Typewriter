#coding=utf-8

import os
from time import sleep
import math
import string

import time

from Adafruit_PWM_Servo_Driver import PWM


pwm = PWM(0x40)



#siffrorna är till för att kalibrera vad nollläge och "aktivt" läge är på servon.
servoMin=[340,440,280,350,340,340,400,570,100,100,100,100]
servoMax=[390,380,330,300,395,280,500,450,100,100,100,100]
servoEnter=800

#600 är noll, 800 enter och 500 mellanslag

#servoMin and servoMax might have to change, and/or introduce more variables since not all servos need to move the same distance,
#This will have to be sorted out when the hardware is in place.

def read_file():

    file = open('text.txt', 'r')

    charList=list(file.read())

    return charList


def printChar(letterIn):
    letters=string.ascii_lowercase+'åäö'
    Special='´+=%?&()":/'
    numbers='1234567890'

    code_numbers=['110100','111111','111010','111011',' 110101','110110', '111100','110010','111000','110111','111101','110011','111001','110000']

    code_letters=['010011','100000','100011','100111','101100','001011','001111','100100','010010','001110','100010','100101','011111','101010','010101','000110','000010','010111','010100','100001','101011','011011','010000','101111','000100','110001','000101','010110','001010']

    code_numbers=['111111','111010','111011','110101','110110','110010','110111','110011','110000','110100']



    if letterIn.lower() in letters and letterIn.isupper():


        controlServo(code_letters[letters.index(letterIn.lower())],True)  #Searches for the input in lowercase since that's the only one that exists.

    elif letterIn.lower() in letters:


        controlServo(code_letters[letters.index(letterIn.lower())], False)
    elif letterIn in numbers:

        controlServo(code_numbers[numbers.index(letterIn)], False)

    elif letterIn in Special:



        controlServo(code_numbers[Special.index(letterIn)], True)

    elif letterIn ==' ':
        pwm.setPWM(7, 0, servoMax[7]) #Sets servo that controls space to its "spaceValue"

        print('Space')

    else:
        print('Not valid')



def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz

  pulseLength /= 4096                     # 12 bits of resolution

  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

def controlServo(code, cap):

    b=[]

    for  digit in str(code):
        b.append(int(digit))




    for x in range(0,6):  #Sets servos to their code.
        #print(code[x])

        if b[x] == 1:
            print(x)
            pwm.setPWM(x,0,servoMax[x])




    if cap==True:
        pwm.setPWM(10,0,servoMax)  #10 is placholder, replace with adress to pwm servo.


        print('Cap')


    strike()



    for x in range (0,6):    #Resets servos to start position.
        pwm.setPWM(x,0,servoMin[x])



        #print('Reset')


    time.sleep(1)

def strike():

    print('Strike')
    time.sleep(0.1)

    pwm.setPWM(x, 0, 330)
    pwm.setPWM(x, 0, 320)


    #Values




def main():

    charList=read_file()

    while True:

        temp=raw_input("Siffra \n")


        printChar(temp) #Should send each character to the printChar function. So add forloop to send letters one and one.


if __name__ == "__main__":
    main()