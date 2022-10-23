# Brackets

Encodes text into binary and then to a special format known as brackets.

**How this new format works?**

There are 2 simple rules:

- `0` corresponds to `(` (Opening bracket)
- `1` corresponds to `)` (Closing bracket)

*For example:*

"Hello world" in binary:

```
01001000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01101100 01100100 00001010
```

"Hello world" in *brackets*:

```
()(()(((())(()()())())((())())((())())))(()(((((()))()))())())))()))(()(())())((())(()(((((()()(
```

## Usage

- Installation

**Prerequisites:** `git`, `python3` and a text editor.

```bash
git clone https://github.com/Sarthak2143/brackets
cd brackets/
# giving executable perms to encoder and decoder.
chmod +x encode.py decode.py
```

- Encoding

Open `input.txt` or any text file in your text editor and add anything that is to be encoded.

Run the encoder afterwards:

```bash
./encode.py -i <input_file> -o <output_file>
```

This will create a new file `<output_file>` as you passed it in the CLI args in the current directory.

- Decoding

Run `decode.py` to reverse the process. 

```bash
./decode.py -i <encoded_file> -o <decoded_file>
```
It'll return a file `<decoded_file>` as you passed the name in CLI args in the same directory. This file will he the same as our `<input_file>`.


## TODO

- [x] Fix Decoder to decode into plain text.
- [x] Use CLI arguments to pass in input and output file.
- [ ] Use more paranthesis.
