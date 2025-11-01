from typing import List, Dict, Optional


# Implement a method that groups strings by their length:
# Requirements
# — Handle null and empty lists → return an empty Map
# — Ignore null elements in the list
# — The order of strings in groups is preserved
# — Group empty strings with key 0
def group_by_length_v1(strings: Optional[List[Optional[str]]]) -> Dict[int, List[str]]:
    if strings is None or len(strings) == 0:
        return {}
    result = {}
    for string in strings:
        if string is None:
            continue
        length = len(string)
        if length not in result:
            result[length] = []
        result[length].append(string)
    return result


def group_by_length(strings: Optional[List[Optional[str]]]) -> Dict[int, List[str]]:
    if not strings:
        return {}
    return {
        length: [s for s in strings if s is not None and len(s) == length]
        for length in {len(s) for s in strings if s is not None}
    }


if __name__ == "__main__":
    # Test case 1: Normal case
    test1 = ["a", "bb", "ccc", "dd", "e", "fff"]
    print(f"Test 1: {group_by_length(test1)}")
    # Output: {1: ['a', 'e'], 2: ['bb', 'dd'], 3: ['ccc', 'fff']}

    # Test case 2: With None elements
    test2 = ["hello", None, "world", "hi", None, "java"]
    print(f"Test 2: {group_by_length(test2)}")
    # Output: {5: ['hello', 'world'], 2: ['hi'], 4: ['java']}

    # Test case 3: With empty strings
    test3 = ["", "test", "", "a"]
    print(f"Test 3: {group_by_length(test3)}")
    # Output: {0: ['', ''], 4: ['test'], 1: ['a']}

    # Test case 4: None list
    test4 = None
    print(f"Test 4: {group_by_length(test4)}")
    # Output: {}

    # Test case 5: Empty list
    test5 = []
    print(f"Test 5: {group_by_length(test5)}")
    # Output: {}

    # Test case 6: Order preservation
    test6 = ["cat", "dog", "ant", "bee", "cow"]
    print(f"Test 6: {group_by_length(test6)}")
    # Output: {3: ['cat', 'dog', 'ant', 'bee', 'cow']}

    # Test case 7: Mixed lengths with order
    test7 = ["python", "is", "awesome", "code", "fun", "programming"]
    print(f"Test 7: {group_by_length(test7)}")
    # Output: {6: ['python'], 2: ['is'], 7: ['awesome'], 4: ['code'], 3: ['fun'], 11: ['programming']}
