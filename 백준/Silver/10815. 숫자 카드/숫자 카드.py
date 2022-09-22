import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int,input().split()))
card.sort()
m = int(input())
info = list(map(int, input().split()))

dict = {}
for i in card:
  dict[i] = 0

for j in info:
  if j not in dict:
    print(0, end=' ')
  else:
    print(1, end=' ')