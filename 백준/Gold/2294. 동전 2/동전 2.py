import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coin=[int(input()) for _ in range(n)]
dp = [10001 for i in range(k+1)]
dp[0] = 0

for i in coin:
  for j in range(i,k+1):
    dp[j] = min(dp[j],dp[j-i]+1)
 
if dp[-1]!=10001:
  print(dp[-1])
else:
  print(-1)