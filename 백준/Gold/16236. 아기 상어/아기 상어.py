#상어위치 저장
#위치정보는 물고기 먹고 난 후 0으로 초기화
#물고기 있는지 체크하는 함수
#물고기 탐색 함수
#물고기 없을 때 까지 잡아먹는 함수

from collections import deque

n=int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

#상어위치 저장
def find():
  for i in range(n):
    for j in range(n):
      if graph[i][j] == 9:
        return i,j

#물고기 여부 확인
def find_fish():
  for i in range(n):
    for j in range(n):
      if 1<=graph[i][j]<=6 :
        return True
  return False

#최종 연산 함수
def solve(x,y):
  global answer
  global size
  eat = 0
  while True:
    fish = bfs(x,y)
    if fish:
      dist,x_shark, y_shark = fish
      graph[x_shark][y_shark] = 0
      eat+=1
      answer += dist
      if eat == size :
        size +=1
        eat = 0
      x = x_shark
      y = y_shark
    else:
      break

#물고기 찾는 함수
def bfs(x,y):
  global size
  visit = [[False]*n for _ in range(n)]
  fish = []
  q = deque()
  q.append((0,x,y))
  while q:
    dist, x, y = q.popleft()
    visit[x][y] = True
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx<n and 0<=ny<n and not visit[nx][ny] :
        visit[nx][ny] = True
        if 1<=graph[nx][ny]<=6 and graph[nx][ny]<size:
          #먹을 수 있을 때
          q.append((dist+1,nx,ny))
          fish.append((dist+1,nx,ny))
        elif graph[nx][ny]==0 or size==graph[nx][ny]:
          #먹을 수 없을 때
          q.append((dist+1,nx,ny))
  if fish :
    return sorted(fish)[0]
  else:
    return False


#실행함수
if find_fish():
  size = 2
  x,y = find()
  dx = [-1,0,0,1]
  dy = [0,-1,1,0]
  graph[x][y] = 0
  answer = 0
  solve(x,y)
  print(answer)
else:
  print(0)