from collections import deque

def bfs(x,y):
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  queue = deque()
  queue.append((x,y))

  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx,ny = x+dx[i],y+dy[i]
      if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
        graph[nx][ny] = graph[x][y]+1
        queue.append((nx,ny))
  return graph[n-1][m-1]
  
n,m = map(int,input().split())
graph=[list(map(int,input())) for _ in range(n)]

print(bfs(0,0))