import os
import shutil
import glob
import sys
import argparse
import re

# Return the current working directory
print(os.getcwd())

# print(dir(os))
# print(help(os))
print(glob.glob("*.py"))

print(sys.argv)

sys.stderr.write('Warning, log file not found starting a new one\n')
# The most direct way to terminate a script is to use sys.exit()

# ['foot', 'fell', 'fastest']
res = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(res)

# 'cat in the hat'
res = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print(res)

# 'tea for two'
print('tea for too'.replace('too', 'two'))


