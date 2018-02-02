"""
Q1 --> Check whether a string has unique characters or not?
Follow up: Without using any data structure
"""

import string
import random

# With data structure
# O(n) time complexity
# O(n) space complexity
def checkIfUnique(string):
    charSet = set([])
    for char in string:
        if char in charSet:
            return False
        else:
            charSet.add(char)
    return True

# Without data structure
# O(n^2) time complexity
# O(1) space complexity

def checkIfUniueNoDS(string):

    for index, current_char in enumerate(string):
        for following_char in string[index+1:]:
            if current_char == following_char:
                return False
    return True

def main():
    for test in range(10):
        input_str = ''.join(random.choice(string.lowercase) for i in range(7))
        flag = len(input_str) == len(set(input_str))
        if flag:
            print input_str, "::Unique::"
        else:
            print input_str, "::Not Unique::"
        assert checkIfUnique(input_str) == flag
        assert checkIfUniueNoDS(input_str) == flag

if __name__ == '__main__':
    main()
