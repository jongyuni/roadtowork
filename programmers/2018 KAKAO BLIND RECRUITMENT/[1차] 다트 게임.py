def solution(dartResult):
  answer = 0
  number = '012345678910'
  bonus = 'SDT'
  option = '*#'
  stack = []
  l = len(dartResult)
  i = 0
  cnt = 2

  while i < l:
    str = dartResult[i:i+cnt]
    if str in number: # str == 10, 1 ..
      stack.append(int(str))
    elif str in bonus:
      if str == 'S':
        stack[-1] = stack[-1] * 1
        cnt = 2
      elif str == 'D':
        stack[-1] = stack[-1] * stack[-1]
        cnt = 2
      else: # str == 'T'
        stack[-1] = stack[-1] * stack[-1] * stack[-1]
        cnt = 2
    elif str in option:
      if str == '*':
        if len(stack) > 1:
          stack[-1] = stack[-1] * 2
          stack[-2] = stack[-2] * 2
          cnt = 2
        elif len(stack) == 1:
          stack[-1] = stack[-1] * 2
          cnt = 2
        else:
          continue
      elif str == '#':
        stack[-1] = stack[-1] * (-1)
        cnt = 2
    else:
      cnt = 1
      i -= 1
    i += 1
    if str == '10':
      i += 1
  answer = stack[-1] + stack[-2] + stack[-3]
  return answer
