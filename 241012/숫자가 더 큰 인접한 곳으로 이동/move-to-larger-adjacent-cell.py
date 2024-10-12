n, curr_x, curr_y = tuple(map(int, input().split()))
a = [[0] * n]
for _ in range(n):
    a.append([0] + list(map(int, input().split())))

dxs, dys = [0,0,-1,1], [1,-1,0,0]

# 종료 조건: 주위에 갈 곳이 없을 때

curr_value = n[curr_x][curr_y]
search_num=0
while search_num < 5:
    for dx, dy in zip(dxs, dys):
        if curr_value < n[curr_x+dx][curr_y+dy]:
            print(n[curr_x+dx][curr_y+dy], end=" ")
            curr_x, curr_y = curr_x+dx, curr_y+dy
            break
        else:
            search_num+=1