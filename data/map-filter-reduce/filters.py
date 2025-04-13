is_A = lambda score: score > 75

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
over_75 = list(filter(is_A, scores))
print(over_75)  # [90, 76, 88, 81]

dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
palindromes = list(filter(lambda word: word == word[::-1], dromes))
print(palindromes)  # ['madam', 'anutforajaroftuna']
