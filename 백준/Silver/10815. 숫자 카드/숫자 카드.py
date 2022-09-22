import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int,input().split()))
card.sort()
m = int(input())
info = list(map(int, input().split()))

def search(arr,target,start,end):

  while start <= end:
    mid = (start+end)//2
    if target == arr[mid]:
      return mid
    elif target<arr[mid]:
      end = mid-1
    else :
      start = mid+1
  return None
 
for i in info:
  if search(card,i,0,n-1) is not None:
    print(1,end=' ')
  else:
    print(0,end=' ')
