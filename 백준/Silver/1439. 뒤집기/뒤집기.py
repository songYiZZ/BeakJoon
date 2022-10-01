s = input()
cnt = 0
temp = s[0]
for i in s:
  if i != temp:
    temp = i
    cnt += 1
if cnt%2==0:
  print(cnt//2)
else :
  print((cnt+1)//2)