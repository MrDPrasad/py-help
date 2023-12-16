def calculate_string_value(input_string):
    # Define a dictionary to map each letter to its corresponding value
    letter_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
                     'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
                     'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

    # Remove spaces from the input string
    input_string = input_string.replace(" ", "")

    # Convert the input string to lowercase for case-insensitivity
    input_string = input_string.lower()

    # Calculate the total value by summing up the values for each character
    total_value = sum(letter_values.get(char, 0) for char in input_string)

    # Continue adding individual digits until a single-digit result is obtained
    while total_value >= 10:
        total_value = sum(map(int, str(total_value)))

    # Display individual values for each character
    char_values = {char: letter_values.get(char, 0) for char in input_string}

    return total_value, char_values

# Get user input
user_input = input("Enter a string: ")

# Calculate the total value and individual values for each character
result, char_values = calculate_string_value(user_input)

# Print the total value
print(f"The total value of the string '{user_input}' is: {result}")

# Print individual values for each character
print("Individual values for each character:")
for char, value in char_values.items():
    print(f"{char} = {value}")
