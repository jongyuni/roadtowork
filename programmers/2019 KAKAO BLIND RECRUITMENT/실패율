def solution(N, stages):
    answer = []
    p = len(stages)
    pis = [0] * (N+2)
    fail = dict()

    for stage in stages:
        pis[stage] += 1

    for i in range(1,N+1):
        if p == 0:
            fail[i] = 0
            continue
        fail[i] = pis[i] * 100 / p
        p -= pis[i]

    return sorted(fail,key=lambda x:fail[x],reverse=True)
