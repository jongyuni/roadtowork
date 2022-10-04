import re

cipher = input()

p = re.compile('(a|e|i|o|u)p(a|e|i|o|u)')
original = p.sub('\\1',cipher)
print(original)
