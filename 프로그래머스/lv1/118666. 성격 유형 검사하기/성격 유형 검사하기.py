def solution(survey, choices):
    answer = ''
    arr = ["RT","CF","JM","AN"]
    dict = {}
    
    for i in arr :
        dict[i[0]] = 0
        dict[i[1]] = 0
    
    for i in range(len(survey)):
        tmp = survey[i]
        if choices[i] < 4:
            dict[tmp[0]]+=(4-choices[i])
        elif choices[i] > 4:
            dict[tmp[1]]+=(choices[i]-4)
    
    for i in arr:
        if dict[i[0]] > dict[i[1]]:
            answer += i[0]
        elif dict[i[0]] < dict[i[1]]:
            answer += i[1]
        else:
            answer += i[0]
    return answer