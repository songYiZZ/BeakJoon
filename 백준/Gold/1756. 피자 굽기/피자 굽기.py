import sys
input = sys.stdin.readline

n,m = map(int,input().split())
oven = list(map(int,input().split()))
pizza = list(map(int, input().split()))

for i in range(1,n):
  oven[i] = min(oven[i],oven[i-1])

idx = 0
depth = n-1

for i in reversed(range(n)):
  if idx >= len(pizza):
    print(depth+1)
    sys.exit(0)

  if oven[i] >= pizza[idx]:
    idx += 1
    depth = i
print(0)