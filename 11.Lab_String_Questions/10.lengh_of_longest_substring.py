'''Q10. Write a Python function to find the length of the longest substring in a given string that contains no repeating characters.
Example:  Input: "abcabcbb" 
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''

def length_of_longest_substring(s):
    char_set = set()  # A set to keep track of unique characters
    start = 0  # The starting point of the window
    max_length = 0  # To store the maximum length
    longest_substring = ""  # To store the longest substring

    for end in range(len(s)):
        # If the character is already in the set, move 'start' to the right
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1

        # Add the current character to the set
        char_set.add(s[end])

        # If we found a longer substring, update the longest substring and its length
        if end - start + 1 > max_length:
            max_length = end - start + 1
            longest_substring = s[start:end+1]

    return max_length, longest_substring

# Take input from the user
input_string = input("Enter a string: ")

# Call the function and print the result in one line
length, substring = length_of_longest_substring(input_string)
print(f'The answer is "{substring}", with the length of "{length}".')