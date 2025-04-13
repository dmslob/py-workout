from typing import List
from collections import Counter


def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Output:
    [['angel', 'glean'], ['car', 'arc'], ['brag', 'grab']]
    """
    grouped_anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in grouped_anagrams:
            grouped_anagrams[sorted_word].append(word)
        else:
            grouped_anagrams[sorted_word] = [word]
    return list(grouped_anagrams.values())


strs = ["angel", "car", "brag", "arc", "glean", "grab"]
out = group_anagrams(strs)
print(out)


def is_anagram(word1: str, word2: str) -> bool:
    if len(w1) != len(word2):
        return False
    # sorted_word1 = ''.join(sorted(word1))
    sorted_word1 = Counter(word1)  # Counter({'c': 1, 'a': 1, 'r': 1})
    # sorted_word2 = ''.join(sorted(word2))
    sorted_word2 = Counter(word2)  # Counter({'a': 1, 'r': 1, 'c': 1})
    return sorted_word1 == sorted_word2


w1 = "car"
w2 = "arc"
print(is_anagram(w1, w2))
