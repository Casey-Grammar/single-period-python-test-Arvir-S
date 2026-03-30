# Task 02a - Count Vowels
# Write a function called count_vowels(text)
# that returns the number of vowels in the string.
# Count both uppercase and lowercase vowels.
#
# Vowels are: a, e, i, o, u
#
# Example:
# count_vowels("Education") -> 5

def count_vowels(text):
    # Write your code here
    count = 0
    vowels = "aeiou"
    for char in text.lower():
        if char in vowels:
            count += 1
    pass


def main():
    text = input("Enter text: ")
    print(count_vowels(text))


if __name__ == "__main__":
    main()
