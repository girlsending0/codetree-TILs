from collections import deque
import sys

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

# bfs에 필요한 변수들 입니다.

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]
# step[i][j] : 시작점으로부터 (i, j) 지점에 도달하기 위한 
# 최단거리를 기록합니다.
step = [
    [0 for _ in range(m)]
    for _ in range(n)
]

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<m and a[x][y]==1

def push(x,y,s):
    step[x][y]= s
    visited[x][y]=True
    q.append((x,y))

INT_MAX=sys.maxsize
ans = INT_MAX

def bfs():
    global ans
    while q:
        x, y = q.popleft()
        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if in_range(new_x, new_y) and not visited[new_x][new_y]:
                push(new_x, new_y, step[x][y]+1)
                #print(visited)

    # 우측 하단에 가는 것이 가능할때만 답을 갱신해줍니다.
    if visited[n - 1][m - 1]:
        ans = step[n - 1][m - 1]

q = deque()
push(0, 0, 0)
bfs()
if ans == INT_MAX:
    ans = -1
    
print(ans)