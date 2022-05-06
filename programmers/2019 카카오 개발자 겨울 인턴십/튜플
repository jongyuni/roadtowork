def solution(s):
  answer = []
  s = s[2:-2]
  s = s.split('},{')
  s.sort(key=len)
  
  for i in s:
    ss = i.split(',')
    for j in ss:
      if int(j) not in answer:
        answer.append(int(j))
        
  return answer
