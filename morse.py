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
# used code from first morse code assessment

from morse_dict import MORSE_2_ASCII


def decode_bits(bits):
    # your code here
    pass


def decode_morse(morse):
    # your code here
    MORSE_2_ASCII
    # your code here
    # strip takes out trailing. spaces in front and back
    morse = morse.strip()
    # splitting by 3 spaces. each word we split is by 3 spaces
    words_list = morse.split("   ")
    w_translate = []
    for word in words_list:
        letter_list = word.split(" ")
        l_translate = []
        for letter in letter_list:
            translate = MORSE_2_ASCII[letter]
            l_translate.append(translate)
        w_translate.append("".join(l_translate))
    result = " ".join(w_translate)

    return result


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
