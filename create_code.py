import csv

dict = {}
for i in range(26):
    # Get the letter from the alphabet
    letter = chr(i + 97)
    # Get the character mapping from the user
    new_letter = input(f"Enter a letter to assign to {letter}: ")
    # Ensure that the input is a valid letter and not already assigned
    while len(new_letter) != 1 or not new_letter.isalpha() or new_letter in dict.values():
        if len(new_letter) != 1 or not new_letter.isalpha():
            print("Invalid input. Please enter a single letter.")
        elif new_letter in dict.values():
            print("This letter is already assigned to another letter.")
        new_letter = input(f"Enter a letter to assign to {letter}: ")
    # Add the mapping to the dictionary
    dict[letter] = new_letter

# Save the dictionary to a csv
with open('code.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write the data
    for key, value in dict.items():
        writer.writerow([key, value])

print()
print("The character mapping has been saved to code.csv.")