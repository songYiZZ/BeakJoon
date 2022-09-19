n,m = map(int,input().split())

s = []
 
def dfs():
    if len(s)==m: #[]에 저장된 원소 갯수가 m개면 출력
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):#0~n까지가 아니라 1~n+1
        if i not in s:#중복이 아니라면 숫자 s에 넣어
            s.append(i)
            dfs()
            s.pop()
 
dfs()
