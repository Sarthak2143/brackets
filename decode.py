#! /usr/bin/env python3

import re
import argparse
import sys

def main():
    "main function"
    # creating the argparser object
    parser = argparse.ArgumentParser(
            description = "Decoder for brackets."
            )
    # adding args
    parser.add_argument(
            "-i",
            "--input",
            type = str,
            nargs = 1,
            metavar = "input_file",
            default = None,
            help = "Adds input file for decoding."
            )
    # adding args for output file 
    parser.add_argument(
            "-o",
            "--output",
            type = str,
            nargs = 1,
            metavar = "output_file",
            default = None,
            help = "Adds output file for decoded data."
            )
    # parsing args from CLI
    args = parser.parse_args()
    if args.input != None and args.output != None:
        decode(args.input[0], args.output[0])
    else:
        sys.stderr.write("No or some arguments were passed. Use the flag '--help' for all flags.\n")
        sys.exit(0)

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
    # running the scrip
    main()
