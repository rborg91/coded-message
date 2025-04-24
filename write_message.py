import csv

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

# Read the original text file message
with open("encode/original_message.txt", "r", encoding="utf-8") as file:
    message = file.read()

# Encode the message
converted_message = encode_message(message, "code.csv")

# Print the encoded message
print()
print("Encoded Message:")
print(converted_message)

# Save the encoded message to a new text file
with open("encode/encoded_message.txt", "w", encoding="utf-8") as file:
    file.write(converted_message)