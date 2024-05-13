# -*- coding: utf-8 -*-
"""
Filename: SteelmanBenjamin_Functions.py 
Author: Benjamin Steelman
DLM: May 12th, 2024
This program includes the functions used within the binary conversion program.
"""
def Conversion_from_Base_Ten(count, number, base, output = []):
    count = number
    while number > 0:
        output.append('0')
        number = number//base
    number = count
    count = 0
    while int(number) > 0:
         if number%base < 10:
             output[count]= str(number % base)
         elif number%base == 10:
             output[count] = 'A'
         elif number%base == 11:
             output[count] = 'B'
         elif number%base == 12:
             output[count] = 'C'
         elif number%base == 13:
             output[count] = 'D'
         elif number%base == 14:
             output[count] = 'E'
         elif number%base == 15:
             output[count] = 'F'
         else:
              number = -1
              output = 'Invalid'
         if not number == -1:
             number = number//base
             count = count + 1
    if not number == -1:
        output.reverse()
        number = str(''.join(output))
    elif number == -1:
        number = 'Invalid'
    return number
# Function to convert from base ten
def Conversion_to_Base_Ten(count, number, base, output, into = []):
    into = list(number)
    while len(into) > count:
        into[count] = into[count]
        count = count + 1
    into.reverse()
    count = 0
    while len(str(number)) > count:
        if base < 10 and into[count] == '1' or base < 10 and into[count] == '2' or base < 10 and into[count] == '3' or base < 10 and into[count] == '4' or base < 10 and into[count] == '5' or base < 10 and into[count] == '6' or base < 10 and into[count] == '7' or base < 10 and into[count] == '8' or base < 10 and into[count] == '9':
            output = output + ((base**count)*int(into[count]))
        elif base > 10 and base < 11 and into[count] == 'A' or base < 11 and into[count] == 'a':
            output = output + ((base**count)*10)
        elif base > 10 and base < 12 and into[count] == 'B' or base > 10 and base < 12 and into[count] == 'b':
            output = output + ((base**count)*11)            
        elif base > 10 and base < 13 and into[count] == 'C' or base > 10 and base < 13 and into[count] == 'c':
            output = output + ((base**count)*12)
        elif base > 10 and base < 14 and into[count] == 'D' or base > 10 and base < 14 and into[count] == 'd':
            output = output + ((base**count)*13)    
        elif base > 10 and base < 15 and into[count] == 'E' or base > 10 and base < 15 and into[count] == 'e':
            output = output + ((base**count)*14)            
        elif base > 10 and base < 16 and into[count] == 'F' or base > 10 and base < 16 and into[count] == 'f':
            output = output + ((base**count)*15)    
        else: 
            number = 1
            count = 2
            output = 'Invalid'
        count = count + 1
    return output
# Function to convert from base ten
def Conversion_from_any_Base_to_Another(Conversion_from_Base_Ten, Conversion_to_Base_Ten, convert, base, baseTwo, intermediate):
    intermediate = Conversion_to_Base_Ten(0, convert, base, 0)
    if intermediate == 'Invalid':
        convert = 'Invalid'
    else:    
        convert = Conversion_from_Base_Ten(0, intermediate, baseTwo)
    return convert
# Conversion to convert from one base to another