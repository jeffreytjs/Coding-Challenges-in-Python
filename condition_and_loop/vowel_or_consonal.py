# Day 17 - Problem 20

# Challenge
# Write a Python program to check whether an alphabet is a vowel or consonant

vowel = ['a', 'e', 'i', 'o', 'u']


def check_letter(n):
    if n in vowel:
        print('This is a vowel!')
    else:
        print('This is a consonant!')
