n, curr_x, curr_y = tuple(map(int, input().split()))
a = [[0] * (n+1)]
for _ in range(n):
    a.append([0] + list(map(int, input().split())))

m = len(a[0])
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

# 종료 조건: 주위에 갈 곳이 없을 때

def in_range(x, y):
    return 0<x and x<=n and y>0 and y<=n

curr_value = a[curr_x][curr_y]

search_num=0
while search_num < 4:
    curr_value = a[curr_x][curr_y]
    print(curr_value, end=" ")
    for dx, dy in zip(dxs, dys):
        if in_range(curr_x+dx, curr_y+dy) and (curr_value < a[curr_x+dx][curr_y+dy]):
            curr_x, curr_y = curr_x+dx, curr_y+dy
            search_num=0
            break
        else:
            search_num+=1