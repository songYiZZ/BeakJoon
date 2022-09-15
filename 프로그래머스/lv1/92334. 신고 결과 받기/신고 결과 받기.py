def solution(id_list, report, k):
    answer = [0]*len(id_list)
    stop=[]
    rpt = {id:[] for id in id_list}

    for i in set(report):
      i = i.split(' ')
      rpt[i[1]].append(i[0])

    for key,value in rpt.items():
        if len(value) >= k:
            for v in value:
                answer[id_list.index(v)] += 1

    return answer