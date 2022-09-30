arr = [500,100,50,10,5,1]
n = int(input())
n = 1000-n
cnt = 0
for i in arr:
  if n>0:
    cnt += n//i
    n = n%i
  else:
    break
print(cnt)