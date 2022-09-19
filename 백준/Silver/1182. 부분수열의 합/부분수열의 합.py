n,s = map(int,input().split())
k = list(map(int,input().split()))
cnt = 0

def backtracking(i,sum):
  global cnt

  #현재 인덱스가 정수의 개수보다 크면 리턴
  if i >= n:
    return

  #수열에 현재 인덱스 더해
  sum+=k[i]

  #현재 수열의 합이 s라면 카운트
  if sum == s:
    cnt += 1

  backtracking(i+1,sum)#다음 인덱스,현재 정수값더한거
  backtracking(i+1,sum-k[i])#다음 인덱스,현재 정수값 안더한거

backtracking(0,0)
print(cnt)