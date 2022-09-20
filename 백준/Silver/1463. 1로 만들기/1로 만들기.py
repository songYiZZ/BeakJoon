import sys
input = sys.stdin.readline

n = int(input())
answer = [0]*1000001

for i in range(2,n+1):
  li = [answer[i-1]]
  if i%3==0:
    li.append(answer[i//3])
  if i%2==0:
    li.append(answer[i//2])
  answer[i] = min(li)+1
  
print(answer[n])