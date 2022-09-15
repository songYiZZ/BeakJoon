def dfs(x,y):
  if x>= n or x<=-1 or y>=n or y<=-1:
    return False

  if graph[x][y] == 1:#아파트 단지경우
    global cnt
    cnt+=1
    graph[x][y]=0 #방문처리
    dfs(x-1,y)#아래
    dfs(x+1,y)#위
    dfs(x,y-1)#왼
    dfs(x,y+1)#오
    return True
  return False

n = int(input())

graph = []
for i in range(n):
  graph.append(list(map(int,input())))

result = 0
cnt = 0
answer=[]
for i in range(n):
  for j in range(n):
    if dfs(i,j) == True:
      result+=1
      answer.append(cnt)
      cnt=0

print(result)
answer.sort()
for i in range(len(answer)):
    print(answer[i])
