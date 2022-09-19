n,m = list(map(int,input().split()))
s = []
def back(start):
  if len(s)==m:
    print(' '.join(map(str,s)))
    return
  for i in range(start,n+1):
    if i not in s:
      s.append(i)
      back(i+1)
      s.pop()

back(1)