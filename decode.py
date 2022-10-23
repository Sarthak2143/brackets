#! /usr/bin/env python3

import re

def decode(input_file, output_file):
    # opening input file in read mode
    with open(input_file, "r") as file:
        data = file.read()
    # we'll add our decoded data in result
    result = ""
    # iterating through data from input file
    for i in data:
        # decoding strings
        if i == "(":
            result += "0"
        elif i == ")":
            result += "1"

    # Initializing the binary string to a int base 2
    binary_int = int(result, 2)
    # getting the byte number 
    byte_number = binary_int.bit_length() + 7 // 8
    # getting an array of bytes 
    array = binary_int.to_bytes(byte_number, "big")
    # converting array to ASCII
    ascii_text = array.decode()

    # opening output file in write mode
    with open(output_file, "w") as out:
        # writing result to output file
        out.write(ascii_text)

if __name__ == "__main__":
    # decoding...
    decode("encoded.txt", "decoded.txt")
