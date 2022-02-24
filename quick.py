from collections import deque

def in_range(x,y):
    return x>=0 and y>=0 and x<n and y<m

def can_go(x,y):
    return in_range(x,y) and not v[x][y] and g[x][y]==0

def bfs():
    dxs,dys=[1,0,-1,0],[0,1,0,-1]
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dxs[i], y+dys[i]
            if can_go(nx,ny):
                v[nx][ny]=1
                q.append((nx,ny))

def change():
    for i in c:
        x=i//m
        y=i%m
        if g[x][y]==2:
            break
        g[x][y]=1
    
    for i in range(n):
        for j in range(m):
            if g[i][j]==2:
            
                q.append((i,j))
                bfs()


def choose(x,p):
    if x==3:
        change()
        return
    for i in range(p,n*m):
        c.append(i)
        choose(x+1,i+1)
        c.pop()


n,m=tuple(map(int, input().split()))
g=[
    list(map(int, input().split()))
    for _ in range(n)
]

v=[
    [0 for _ in range(m)]
    for _ in range(m)
]
c=[]
q=deque()
choose(0,0)
print(v)
