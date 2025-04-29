import csv
import time

def check_character_mapping(csv_file):
    """
    Check to see that all 26 letters of the alphabet are present in the CSV file
    in the key and value column.

    Parameters:
    csv_file (str): The path to the CSV file containing character mappings.
    """
    
    # Read the CSV file which contains the character mappings
    with open(csv_file, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        conversion_dict = {rows[0]: rows[1] for rows in reader}

    # Check if all letters are present in the key and value columns
    keys = set(conversion_dict.keys())
    values = set(conversion_dict.values())
    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    missing_keys = alphabet - keys
    missing_values = alphabet - values

    if missing_keys or missing_values:
        print("There is an issue detected with the character mapping in the CSV file.")
        print("Please check the CSV file to see that all letters of the alphabet")
        print("are present in both the key and value columns.")
        exit(1)
    else:
        print("No issues detected with the character mapping.")

def decode_message(coded_message, csv_file):
    """
    Decode a coded message using a CSV file that contains character mappings.

    Parameters:
    coded_message (str): The message to decode.
    csv_file (str): The path to the CSV file containing character mappings.
    """
    
    # Read the CSV file which contains the character mappings
    with open(csv_file, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        conversion_dict = {rows[0]: rows[1] for rows in reader}

    # Extend the conversion dictionary to handle capital letters
    extended_conversion_dict = {}
    for key, value in conversion_dict.items():
        extended_conversion_dict[value] = key
        if key.islower():
            extended_conversion_dict[value.upper()] = key.upper()

    # Convert the characters to decode the message
    converted_message = []
    for char in coded_message:
        if char in extended_conversion_dict:
            converted_message.append(extended_conversion_dict[char])
        else:
            converted_message.append(char)

    return "".join(converted_message)

# Check the character mapping in the CSV file
print()
print("Checking character mapping in the CSV file...")
time.sleep(2)
check_character_mapping("code.csv")

# Read the original coded text file message
with open("decode/coded_message.txt", "r", encoding="utf-8") as file:
    coded_message = file.read()

# Decode the message
converted_message = decode_message(coded_message, "code.csv")

# Print the decoded message
print()
print("Decoding the message...")
time.sleep(2)
print()
print("Decoded Message:")
print(converted_message)

# Save the decoded message to a new text file
with open("decode/decoded_message.txt", "w", encoding="utf-8") as file:
    file.write(converted_message)
print()
print("Decoded message saved to decode/decoded_message.txt")