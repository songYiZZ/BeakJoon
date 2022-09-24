n = int(input())
graph = [list(map(str,input())) for _ in range(n)]

sum = 0
for i in graph:
  tmp =0
  for j in i:
    if j == 'O':
      tmp += 1
    if j == 'X':
      tmp = 0
    sum += tmp
  print(sum)
  sum=0