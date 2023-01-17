def solution(storey):
    answer = 0

    while storey > 0:
        r = storey % 10

        if 0 < r < 5:
            answer += r
            storey -= r
        elif 5 < r < 10:
            answer += 10 - r
            storey += 10 - r
        else:
            q = storey // 10
            if q % 10 >= 5:
                storey += r
            else:
                storey -= r
            answer += r
            
        storey = storey // 10
        
    return answer
