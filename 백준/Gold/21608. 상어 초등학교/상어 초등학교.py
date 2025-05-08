import sys
input = sys.stdin.readline

N = int(input())

grid = [[0] * N for _ in range(N)]
mw_lst = [0] * (N**2 + 1)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for _ in range(N**2):
    num, *like_lst = map(int, input().split())
    mw_lst[num] = like_lst

    max_likes = -1
    max_blank = -1
    max_y, max_x = -1, -1

    for y in range(N):
        for x in range(N):
            if grid[y][x] == 0:
                likes = 0
                blank = 0

                for d in range(4):
                    ny, nx = y + dy[d], x + dx[d]
                    if 0 <= ny < N and 0 <= nx < N:
                        if grid[ny][nx] in like_lst:
                            likes += 1
                        elif grid[ny][nx] == 0:
                            blank += 1

                if (likes > max_likes or
                   (likes == max_likes and blank > max_blank) or
                   (likes == max_likes and blank == max_blank and (max_y == -1 or y < max_y or (y == max_y and x < max_x)))):
                    max_likes = likes
                    max_blank = blank
                    max_y, max_x = y, x

    grid[max_y][max_x] = num

result = 0
for y in range(N):
    for x in range(N):
        cnt = 0
        A = grid[y][x]
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N and grid[ny][nx] in mw_lst[A]:
                cnt += 1
        if cnt > 0:
            result += 10 ** (cnt - 1)

print(result)
