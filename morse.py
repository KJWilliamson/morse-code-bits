#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Morse Code Decoder
"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
__author__ = 'kamela williamson'
# Got help from April
# collaborated with judy
# used code from first morse code assessment
# rewatched Daniels' morse code demo
# did the morse code advanced on codewars
# https://www.geeksforgeeks.org/python-regex-re-search-vs-re-findall/
# https://www.w3schools.com/python/python_regex.asp
# https://www.w3schools.com/python/ref_string_strip.asp
# https://www.w3schools.com/python/ref_string_split.asp
# https://www.geeksforgeeks.org/morse-code-translator-python/
# https://blog.finxter.com/a-simple-python-morse-code-translator/
# https://www.geeksforgeeks.org/morse-code-implementation/


import re
from morse_dict import MORSE_2_ASCII
# starts with 0's and 1's first. get from 0's and 1's to
# dots and dashes. standard was dots and dashes to alphabet. not
# receiving same input as standard. there's a pattern that maps to dots &
# dashes. and a variable factor.  how fast operator was pushing key
# switch matters.


def decode_bits(bits):
    # your code here
    bits = bits.strip('0')
    # find the least amount of times that 0 or 1 comes up
    tm = min(len(mc) for mc in re.findall(r'1+|0+', bits))
    str = bits[::tm].replace('111', '-').replace('1', '.').replace(
          '0000000', '   ').replace('000', ' ').replace('0', '')
    return str


def decode_morse(morse):
    w_translate = []
    for morse_word in morse.split('   '):
        word = ''.join(MORSE_2_ASCII.get(morse_char, '')
                       for morse_char in morse_word.split(' '))
        if word:
            w_translate.append(word)
    return ' '.join(w_translate)


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "11001100110011000000110000001111110011001111110011111100000000000000000000011001111110011111100111111000000110011001111110000001111110011001100000011" # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
