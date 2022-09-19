graph = [list(input().strip()) for _ in range(8)]
sum = 0
for i in range(0,8):
  for j in range(0,8):
    if (i+j)%2==0 and graph[i][j]=='F':
      sum+=1  
print(sum)
