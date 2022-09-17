import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(x,y):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  visit[x][y]=True
  for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx<n and 0<=ny<n and graph[x][y]==graph[nx][ny] and not visit[nx][ny]:
        dfs(nx,ny)

n=int(input())
graph = [list(map(str,input())) for _ in range(n)]
visit = [[False]*n for _ in range(n)]
cnt1 = 0
cnt2 = 0
for i in range(n):
  for j in range(n):
    if not visit[i][j] :
      cnt1+=1
      dfs(i,j)

visit = [[False]*n for _ in range(n)]
for i in range(n):
  for j in range(n):
    if graph[i][j] == 'R' :
      graph[i][j] = 'G'

for i in range(n):
  for j in range(n):
    if not visit[i][j] :
      cnt2+=1
      dfs(i,j)
      
print(cnt1)
print(cnt2)