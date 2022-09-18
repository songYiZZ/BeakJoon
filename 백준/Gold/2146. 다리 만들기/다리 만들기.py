import sys
from collections import deque
sys.setrecursionlimit(10**6)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = sys.maxsize
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(i,j):
  global cnt
  if i<0 or i>=n or j<0 or j>=n:
      return False
  if graph[i][j] == 1:
      graph[i][j] = cnt
      for z in range(4):
        nx = i+dx[z]
        ny = j+dy[z]
        dfs(nx,ny)
      return True

def bfs(k):
  global answer
  visit = [[-1]*n for _ in range(n)]
  q = deque()

  for i in range(n):
    for j in range(n):
      if graph[i][j]==k:
        q.append((i,j))
        visit[i][j] = 0
  while q:
      x,y = q.popleft()
      for z in range(4):
          nx = x+dx[z]
          ny = y+dy[z]
          if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
          if graph[nx][ny]>0 and graph[nx][ny] != k:
              answer = min(answer,visit[x][y])
              return
          if graph[nx][ny]==0 and visit[nx][ny]==-1:
              visit[nx][ny]= visit[x][y]+1
              q.append((nx,ny))
            
cnt = 2
for i in range(n):
  for j in range(n):
    if dfs(i,j)==True:
      cnt+=1
      
for i in range(2,cnt):
  bfs(i)
print(answer)