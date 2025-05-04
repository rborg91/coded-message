# Coded Messages

## Create a secret coded message or decode one

Decode or encode `.txt` messages based on character mapping located in a `.csv`
file. Currently can only encode or decode English letter characters and not
other symbols such as `.`, `!`, etc.
Keeps capital lettering the same as the original message.

## Requirements

- Python

## Usage

Clone this repository to your local machine and change into your directory.

### Update the character mapping

The character mapping must be located in a file called `code.csv`.

There are various ways to update the character mapping:

- Open the `code.csv` file with a suitable program and manually update
  each character mapping yourself. Please note that column 1 should be kept as is,
  with the character mapping being changed in column 2.
- Run `python create_code.py` and follow the instructions.

### Decode the message

1. Ensure the message that needs to be decoded is saved as `decode/coded_message.txt`.
2. Run `python read_message.txt`.
3. The decoded message will both print in the terminal as well as be saved
   as `decode/decoded_message.txt`.

### Encode the message

1. Ensure the message that needs to be encoded is saved as `encode/original_message.txt`.
2. Run `python write_message.txt`.
3. The encoded message will both print in the terminal as well as be saved
   as `encode/encoded_message.txt`.
