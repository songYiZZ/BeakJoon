import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def dfs(x,y,h):
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if (0<=nx<n) and (0<=ny<n) and not visit[nx][ny] and graph[nx][ny] > h:
      visit[nx][ny] = True
      dfs(nx,ny,h)

n= int(input())
graph=[list(map(int,input().split())) for _ in range(n)]

max_safe = 0
for h in range(max(map(max,graph))):
  visit = [[False] * n for _ in range(n)]
  cnt=0
  for i in range(n):
    for j in range(n):
      if not visit[i][j] and graph[i][j] > h:
        visit[i][j] = True
        dfs(i,j,h)
        cnt+=1
  if max_safe < cnt : max_safe = cnt
print(max_safe)