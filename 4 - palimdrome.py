# Checks if a given string is palimdrome (case insensitive)

def is_palindrome(s):
    return s.lower() == s.lower()[::-1]