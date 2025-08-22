'''
Create a function named find_occurrences that:

Takes two string arguments: text and pattern
Counts how many times pattern appears in text, including overlapping occurrences
Returns a tuple containing:
A boolean indicating if the pattern was found (True/False)
The number of occurrences of the pattern
A list of starting positions where the pattern was found
For example, if text is "abababab" and pattern is "aba", your function should return (True, 3, [0, 2, 4]), since "aba" appears at positions 0, 2, and 4.

If the pattern is not found, return (False, 0, []).
'''
def find_occurrences(text, pattern):
    # Write your code here
    positions = []
    index = 0

    while index <= len(text) - len(pattern):
        if text[index:index + len(pattern)] == pattern:
            positions.append(index)
        index += 1

    found = len(positions) > 0
    return (found, len(positions), positions)


# Read input
text = input()
pattern = input()

# Call your function and print the result
result = find_occurrences(text, pattern)
print(result)