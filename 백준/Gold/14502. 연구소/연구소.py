from collections import deque
import copy

def bfs():
  visit = copy.deepcopy(graph)
  queue = deque()
  for i in range(n):
    for j in range(m):
      if visit[i][j] == 2:
        queue.append((i,j))

  while queue:
    x,y=queue.popleft()

    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx<n and 0<=ny<m and visit[nx][ny]==0:
        visit[nx][ny]=2
        queue.append((nx,ny))
  global answer
  cnt = 0
  for i in range(n):
    cnt += visit[i].count(0)
  answer = max(cnt,answer)

def dfs_wall(cnt):
  if cnt == 3 :
    bfs()
    return
  
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        graph[i][j] = 1
        dfs_wall(cnt+1)
        graph[i][j] = 0


n,m = list(map(int, input().split()))
graph=[list(map(int,input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
  
answer = 0
dfs_wall(0)
print(answer)