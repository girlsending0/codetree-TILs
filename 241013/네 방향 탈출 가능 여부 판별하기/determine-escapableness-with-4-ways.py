from collections import deque

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

dxs, dys= [-1, 1, 0 ,0], [0,0,-1,1] # 상하 좌우

def can_go(x, y):
    return 0<=x and x<n and y>=0 and y<m and not visited[x][y] and a[x][y]

def bfs():
    # bfs 로직
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            if can_go(new_x, new_y):
                q.append((new_x, new_y))
                visited[new_x][new_y]=True

q = deque()
q.append((0, 0))
visited[0][0]= True
bfs()
# print(visited)
if visited[-1][-1]:
    print(1)
else:
    print(0)