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
    # wrapping result into chunks of 8
    result = re.findall("........?", result)
    string = ""
    # adding them to a string with spaces
    for i in result:
        string += i + " "
    # opening output file in write mode
    with open(output_file, "w") as out:
        # writing result to output file
        # with removing extra blank space
        out.write(string[:len(string)-1])

if __name__ == "__main__":
    # decoding...
    decode("encoded.txt", "decoded.txt")
