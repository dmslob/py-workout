# Sliding Window Algorithm
# https://builtin.com/data-science/sliding-window-algorithm
# COUNT OCCURRENCES OF ANAGRAM
# Given a word and a text, return the count of occurrences
# of the anagrams of the word in the text.
# text = "gotxxotgxdogt"
# word = "got"
# Words 'got', 'otg' and 'ogt' are anagrams of 'got'.
# output = 3
def is_anagram(s, word):
    if len(s) != len(word):
        return False
    d = [0] * 26
    for c in s:
        d[ord(c) - ord('a')] = 1
    for c in word:
        if d[ord(c) - ord('a')] == 0:
            return False
    return True


def count_anagram(text, word):
    w = len(word)
    count = 0
    ana = ''
    d = {}
    for i in range(w):
        ana += text[i]

    if is_anagram(ana, word):
        count += 1

    for i in range(1, len(text)):
        ana = ana[1:] + text[i]

        if ana not in d and is_anagram(ana, word):
            count += 1
            d[ana] = 0
        d[ana] = 0

    return count


input_text = "gotxxotgxdogt"
input_word = "got"

output = count_anagram(input_text, input_word)
print(f"Count of '{input_word}' anagram is {output}")