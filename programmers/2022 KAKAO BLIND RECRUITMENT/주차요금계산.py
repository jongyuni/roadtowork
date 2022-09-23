import math

def solution(fees, records):
    answer = []
    logs = dict()
    MAX_TIME = 23*60 + 59
    
    for record in records:
        time, carnum, status = record.split()
        h, m = map(int, time.split(":"))
        t = h*60 + m
        if status == "IN":
            t = t*(-1)
        
        if carnum not in logs:
            logs[carnum] = t
            continue
        else:
            logs[carnum] += t
        
    sorted_logs = dict(sorted(logs.items()))
    
    for value in sorted_logs.values():
        sum = 0
        if value <= 0:
            value += MAX_TIME
        if value <= fees[0]:
            sum += fees[1]
        else:
            sum += fees[1]
            value = math.ceil((value-fees[0])/fees[2])
            sum += value*fees[3]
        answer.append(sum)
            
    return answer
