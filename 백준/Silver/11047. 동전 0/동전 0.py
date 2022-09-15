N, K = map(int, input().split())
array = list()

for i in range(N):
  array.append(int(input()))

cnt = 0
for i in reversed(range(N)):
  cnt += K//array[i]
  K = K%array[i]

print(cnt)