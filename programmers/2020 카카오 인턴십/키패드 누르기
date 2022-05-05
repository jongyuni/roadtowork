def solution(numbers, hand):
    answer = ''
    keypad = {1: [0,0], 2: [0,1], 3: [0,2],
             4: [1,0], 5: [1,1], 6: [1,2],
             7: [2,0], 8: [2,1], 9: [2,2],
             '*': [3,0], 0: [3,1], '#': [3,2]}
    leftonly = [1,4,7]
    rightonly = [3,6,9]
    cur_l = keypad['*']
    cur_r = keypad['#']

    for num in numbers:
        if num in leftonly:
            answer += 'L'
            cur_l = keypad[num]
        elif num in rightonly:
            answer += 'R'
            cur_r = keypad[num]
        else:
            ll = abs(keypad[num][0] - cur_l[0]) + abs(keypad[num][1] - cur_l[1])
            rl = abs(keypad[num][0] - cur_r[0]) + abs(keypad[num][1] - cur_r[1])
            if ll < rl:
                answer += 'L'
                cur_l = keypad[num]
            elif ll > rl:
                answer += 'R'
                cur_r = keypad[num] 
            else:
                if hand == 'right':
                    answer += 'R'
                    cur_r = keypad[num] 
                else:
                    answer += 'L'
                    cur_l = keypad[num]

    return answer
