import re

answer = []
while True:
    tmp = input()
    if tmp == '#':
        break
    p = re.compile('[aeiouAEIOU]')
    result = p.findall(tmp)
    answer.append(len(result))

for a in answer:
    print(a)
