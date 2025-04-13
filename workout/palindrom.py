def is_palindrome_v1(s: str) -> bool:
    """
    Brute force solution
    :param s: string to check
    :return: True if string is palindrome
    """
    original = s
    s = s[::-1]
    return original == s


ss = "kayak"
print(is_palindrome_v1(ss))


# A phrase is a palindrome if,
# after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
# Given a strings, return true if it is a palindrome, or false otherwise.
# Time: O(n)
# Space: O(1)
def is_palindrome_v2(s: str) -> bool:
    n = len(s)
    left = 0
    right = n - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


s2 = "A man, a plan, a canal: Panama"
print(is_palindrome_v2(s2))