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

def encode_message(message, csv_file):
    """
    Encode a message using a CSV file that contains character mappings.

    Parameters:
    message (str): The message to encode.
    csv_file (str): The path to the CSV file containing character mappings.
    """
    
    # Read the CSV file which contains the character mappings
    with open(csv_file, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        conversion_dict = {rows[0]: rows[1] for rows in reader}

    # Extend the conversion dictionary to handle capital letters
    extended_conversion_dict = {}
    for key, value in conversion_dict.items():
        extended_conversion_dict[key] = value
        if key.islower():
            extended_conversion_dict[key.upper()] = value.upper()

    # Convert the characters to encode the message
    converted_message = []
    for char in message:
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

# Read the original text file message
with open("encode/original_message.txt", "r", encoding="utf-8") as file:
    message = file.read()

# Encode the message
converted_message = encode_message(message, "code.csv")

# Print the encoded message
print()
print("Encoding the message...")
time.sleep(2)
print()
print("Encoded message:")
print(converted_message)

# Save the encoded message to a new text file
with open("encode/encoded_message.txt", "w", encoding="utf-8") as file:
    file.write(converted_message)
print()
print("Encoded message saved to 'encode/encoded_message.txt'")