import re

def DecodeRomanNum(romanNum):
    """Decode roman numerals to normal numbers for values >0 and <4000"""
    
    Definitions = {'MMM':3000, 'MM':2000, 'M':1000,
    'CM':900, 'DCCC':800, 'DCC':700, 'DC':600, 'D':500, 'CD':400, 'CCC':300, 'CC':200, 'C':100,
    'XC':90, 'LXXX':80, 'LXX':70, 'LX':60, 'L':50, 'XL':40, 'XXX':30, 'XX':20, 'X':10,
    'IX':9, 'VIII':8, 'VII':7, 'VI':6, 'V':5, 'IV':4, 'III':3, 'II':2, 'I':1}
    
    pattern = re.compile(r'^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
    try:
        foundOrNot = pattern.search(romanNum)
    except TypeError:
        return "You must enter a string!"
    else:
        if foundOrNot == None:
            return "Roman numeral is either not valid or not greater than 0/less than 4000."
        else:
            separation = foundOrNot.groups()
            result = 0
            for numerals in separation:
                if numerals in Definitions:
                    result += Definitions[numerals]
            return str(result)
                    
def EncodetoRomanNum(number):
    """Encode normal numbers to roman numerals for numbers >0 and <4000"""
    
    Conversions ={3000: 'MMM', 2000: 'MM', 1000: 'M', 900: 'CM', 800: 'DCCC', 700: 'DCC', 600: 'DC', 
    500: 'D', 400: 'CD', 300: 'CCC', 200: 'CC', 100: 'C', 90: 'XC', 80: 'LXXX', 70: 'LXX', 
    60: 'LX', 50: 'L', 40: 'XL', 30: 'XXX', 20: 'XX', 10: 'X', 9: 'IX', 8: 'VIII', 7: 'VII', 
    6: 'VI', 5: 'V', 4: 'IV', 3: 'III', 2: 'II', 1: 'I'}
    
    pattern = re.compile(r'^([0-3]?)([0-9]?)([0-9]?)([0-9])$')
    try:
        Split = pattern.search(number)
    except TypeError:
        return "You must enter a string!"
    else:
        if Split == None:
            return "Inserted string either not a number or not greater than 0/less than 4000."
        else:
            separation = Split.groups()
            RomanNum = ''
            for i in range(len(separation)):
                tempNum = 0
                if i == 0 and separation[i] != '':
                    tempNum = int(separation[i]) * 1000
                    RomanNum += Conversions[tempNum]
                elif i == 1 and separation[i] != '':
                    tempNum = int(separation[i]) * 100
                    RomanNum += Conversions[tempNum]
                elif i == 2 and separation[i] != '':
                    tempNum = int(separation[i]) * 10
                    RomanNum += Conversions[tempNum]
                elif i == 3 and separation[i] != '':
                    tempNum = int(separation[i])
                    RomanNum += Conversions[tempNum]     
            return RomanNum

