#! /usr/bin/env python3

#Importing regex i.e Regular Expressions
import re

def main():
    # main function
    binary = text_to_binary("input.txt")
    binary_to_brackets(binary, "encoded.txt")

def binary_to_brackets(data, output_file):
    """
    Processes binary into brackets.
    """
    # we'll add our decoded data in result
    result = ""
    # iterating through data from input file
    for i in data:
        # decoding strings
        if i == "0":
            result += "("
        elif i == "1":
            result += ")"
    # opening output file in write mode
    with open(output_file, "w") as out:
        # writing result to output file
        out.write(result)

def text_to_binary(input_file):
    """
    Processes text into binary.
    """
    # opening file
    with open(input_file, "r") as file:
        txt = file.read()
    # converting text to bin
    res = "".join(format(ord(i), '08b') for i in txt)
    # wrapping res into chunks of 8
    res = re.findall("........?", res)
    result = ""
    # adding spaces in b/w 8 chars
    for i in res:
        result += i + " "
    # returning with removing extra space
    return result[:len(result)-1]

if __name__ == "__main__":
    # running script
    main()
