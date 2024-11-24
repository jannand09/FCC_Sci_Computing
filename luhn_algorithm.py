# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 13:14:45 2024

@author: janna
"""

def verify_card_number(card_number):
    '''
    Verify a card or account number using the Luhn algorithm, which doubles
    every other digit starting from the end and checking if sum of digits
    is a multiple of 10

    Parameters
    ----------
    card_number : str
        card number to verify is valid according to Luhn algorithm

    Returns
    -------
    Boolean
        returns TRUE if number is valid

    '''
    card_number_reversed = card_number[::-1]
    
    sum_of_odd_digits = 0
    odd_digits = card_number_reversed[::2]
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main():
    card_number = '6011-0035 3505 8652'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()