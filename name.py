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
    total_value = sum(letter_values[char] for char in input_string if char in letter_values)

    return total_value

# Get user input
user_input = input("Enter a string: ")

# Calculate and print the total value of the input string
result = calculate_string_value(user_input)
print(f"The total value of the string '{user_input}' is: {result}")
