from collections import Counter
from scipy import stats


def find_mode(nums):
    modes = []
    mode_dict = {}
    max_mode = 0
    for n in nums:
        mode_cnt = 0
        if n in mode_dict:
            mode_cnt = mode_dict[n] + 1
        else:
            mode_cnt = 1
        mode_dict[n] = mode_cnt
        if mode_cnt > max_mode:
            max_mode = mode_cnt
    for k, v in mode_dict.items():
        if v == max_mode:
            modes.append(k)
    return modes


values = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
print(find_mode(values))

mode = stats.mode(values)
print(mode)

n_num = [1, 2, 3, 4, 5, 5]
n = len(n_num)

data = Counter(n_num)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "Mode is / are: " + ', '.join(map(str, mode))

print(get_mode)

# output: [('a', 3), ('b', 3)]
data = "aabbccabc"
cnt = Counter(data)
print(cnt.most_common(2))
