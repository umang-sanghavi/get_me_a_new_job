"""
Q: Given two strings, check if one is a permutation of the other

Thoughts:
A string is a permutation of another means it should have exactly same chars
"""

# With Data structure
# O(n) time complexity
# O(n) space complexity

def checkIfPermuation(string1, string2):

    #short circuit
    if len(string1) != len(string2):
        return  False

    string_dict = {}
    for char in string1:
        if char in string_dict:
            string_dict[char] += 1
        else:
            string_dict[char] = 1

    for char in string2:
        if char in string_dict:
            string_dict[char] -= 1
        else:
            return False # A char of string 2 is not present in string 1
    for val in string_dict.itervalues():
        if val != 0:
            return False
    return True


def main():
    print checkIfPermuation('abcdefghiaa', 'defghiabcab')

if __name__ == '__main__':
    main()
