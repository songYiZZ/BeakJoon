n = int(input())
arr = list(map(int,input().split()))
arr.sort(reverse=False)
newarr = arr.copy()
newarr.sort(reverse=True)

sum = 10000000
for i in range(n):
  sum = min(sum,(arr[i]+newarr[i]))

print(sum)
