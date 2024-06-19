N = int(input())
x, y = 0, 0
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]

# 0 => W
# 1 => S
# 2 => N
# 3 => E

for i in range(N):
    direction, num = input().split()
    num = int(num)
    if direction=='W':
        x, y = x + num*dx[0], y + num*dy[0]

    elif direction=='S':
        x, y = x + num*dx[1], y + num*dy[1]

    elif direction=='N':
        x, y = x + num*dx[2], y + num*dy[2]

    elif direction=='E':
        x, y = x + num*dx[3], y + num*dy[3]

print(x, y)