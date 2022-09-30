n = int(input())
arr = list(map(int,input().split()))
arr.sort()
sum = 0
temp = 0
for i in arr:
  temp += i
  sum = sum + temp
print(sum)
