import os
from time import sleep
import math
import string
#from Adafruit_PWM_Servo_Driver import PWM
import time


#siffrorna är till för att kalibrera vad nollläge och "aktivt" läge är på servon.
servoMin=[100,100,100,100,100,100,450,600,100,100,100,100]
servoMax=[550,550,550,550,100,100,550,500,100,100,100,100]
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
    Special=' #'
    numbers='1234567890'

    code_numbers=['110100','111111','111010','111011',' 110101','110110', '111100','110010','111000','110111','111101','110011','111001','110000']

    code_letters=['010011','100000','100011','100111','101100','001011','001111','100100','010010','001110','100010','100101','011111','101010','010101','000110','000010','010111','010100','100001','101011','011011','010000','101111','000100','010001','110001','000101','010110','001010']


    if letterIn.lower() in letters and letterIn.isupper():

        print('Versal')
        controlServo(code_letters[letters.index(letterIn.lower())],True)  #Searches for the input in lowercase since that's the only one that exists.

    elif letterIn.lower() in letters:

        print('Gemener')
        controlServo(code_letters[letters.index(letterIn.lower())], False)
    elif letterIn in numbers:
        print('Number')
    elif letterIn in Special:

        if letterIn ==' ':
            #pwm.setPWM(7, 0, servoMax[7]) #Sets servo that controls space to its "spaceValue"

            print(' ')

        print('Special')
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


    for x in range(0,6):  #Sets servos to their code.
        print(code[x])

        #pwm.setPWM(x,0,servoMax[x])


    if cap==True:
        #pwm.setPWM(10,0,servoMax)  #10 is placholder, replace with adress to pwm servo.


    #pwm.setPWM(11,0,servoMax)   #10 is placeholder, replace with adress to strike servo.

        print(' ')





    for x in range (0,6):    #Resets servos to start position.
        #pwm.setPWM(x,0,servoMax[x])


        print('Test')





def main():

    charList=read_file()

    printChar(' ') #Should send each character to the printChar function. So add forloop to send letters one and one.


if __name__ == "__main__":
    main()