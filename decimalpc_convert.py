#!/usr/bin/python3

def decimal_to_three_eight_three(num):

    if num<0:
        return False

     # convert number into binary first
    binary = bin(num)
     # remove first two characters
    binary = binary[2:]



    if len(binary)==11:
        # extract last 3 bits
        startLast3bits= 8
        endLast3bits = 12
        last3bits = binary[startLast3bits : endLast3bits]

        # convert extracted last 3bits into decimal back
        decFormOfLast3digits=int(last3bits,2)

        #extract middle8bits
        startMiddle8bits= 0
        endMiddle8bits= 8
        middle8bits = binary[startMiddle8bits : endMiddle8bits]

        # convert extracted middle 8bits into decimal back
        decFormOfMiddle8digits=int(middle8bits,2)

        return '0-%d-%d' %(decFormOfMiddle8digits,decFormOfLast3digits)

    elif len(binary)>11 and len(binary)<=14:
        # extract last 3 bits
        startLast3bits=len(binary)-3
        endLast3bits =len(binary)
        last3bits = binary[startLast3bits : endLast3bits]

        # convert extracted last 3bits into decimal back
        decFormOfLast3digits=int(last3bits,2)

        #extract middle8bits
        startMiddle8bits=len(binary)-11
        endMiddle8bits=len(binary)-3
        middle8bits = binary[startMiddle8bits : endMiddle8bits]

        # convert extracted middle 8bits into decimal back
        decFormOfMiddle8digits=int(middle8bits,2)


        #extract first3bits
        startFirst3bits=0
        startFirst8bits=len(binary)-11
        first3bits = binary[startFirst3bits : startFirst8bits]

        # convert extracted first 3bits into decimal back
        decFormOfFirst3digits=int(first3bits,2)

        return '%d-%d-%d' %(decFormOfFirst3digits,decFormOfMiddle8digits,decFormOfLast3digits)

    elif len(binary)<11 and len(binary)>3:
        # extract last 3 bits
        startLast3bits=len(binary)-3
        endLast3bits =len(binary)
        last3bits = binary[startLast3bits : endLast3bits]

        # convert extracted last 3bits into decimal back
        decFormOfLast3digits=int(last3bits,2)

        # extract binary length until last 3 bits
        startMiddle8bits=0
        endMiddle8bits=len(binary)-3
        middle8bits = binary[startMiddle8bits : endMiddle8bits]

        # convert extracted binary length until last 3 bits
        decFormOfMiddle8digits=int(middle8bits,2)

        return '0-%d-%d' %(decFormOfMiddle8digits,decFormOfLast3digits)
    elif len(binary)<=3:
        # extract last 3 digits only
        startLast3bits=0
        endLast3bits =len(binary)
        last3bits = binary[startLast3bits : endLast3bits]

        # convert extracted last 3bits into decimal back
        decFormOfLast3digits=int(last3bits,2)

        return '0-0-%d' %(decFormOfLast3digits)
    else:
        return 'You entered invalid Point Code decimal value: %d however it should in the range of 0-16383 according to ITU specification' %(num)

import PySimpleGUI as sg


if __name__ == "__main__":
    value = input("Please enter decimal point code: ")
    pc=int(value)

    pcformatin3_8_3=decimal_to_three_eight_three(pc)
    print(pcformatin3_8_3)
