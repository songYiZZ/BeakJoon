n = int(input())
graph = []

for i in range(n):
  tmp = list(map(int,input().split()))
  num = tmp[0]
  avg = int((sum(tmp)-num)/num)
  cnt = 0
  for j in range(1,num+1):
    if tmp[j] > avg:
      cnt+=1
  answer = round((cnt/num)*100,3)
  print("{:.3f}%".format(answer))