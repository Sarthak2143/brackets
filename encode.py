#! /usr/bin/env python3

import re
import argparse
import sys

def main():
    # main function
    # creating the ArgParser Object
    parser = argparse.ArgumentParser(
            description = "Encoder for brackets."
            )
    # adding args
    # adding args for input file 
    parser.add_argument(
            "-i",
            "--input",
            type = str,
            nargs = 1,
            metavar = "input_file",
            default = None,
            help = "Adds input file for encoding."
            )
    # adding args for output file 
    parser.add_argument(
            "-o",
            "--output",
            type = str,
            nargs = 1,
            metavar = "output_file",
            default = None,
            help = "Adds output file for encoded data."
            )
    # parsing args from CLI
    args = parser.parse_args()
    if args.input != None and args.output != None:
        binary = text_to_binary(args.input[0])
        binary_to_brackets(binary, args.output[0])
    else:
        sys.stderr.write("No or some arguments were passed. Use the flag '--help' for all flags.\n")
        sys.exit(1)

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
    try:
        with open(input_file, "r") as file:
            txt = file.read()
    except FileNotFoundError:
        sys.stderr.write(f"File: {input_file} not found.\n")
        sys.exit(1)
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
