import sys
# sys.stdin = open("C:/Users/SSAFY/Desktop/mwalgo/Algorithm/input.txt", 'r')
input = sys.stdin.readline

import copy
#입력처리
N, M, R= map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

# 돌리고 돌리고~
def doligo(N,M,grid,cx,cy):
  # 반시계 (하 우 상 좌 )
  global visited
  directions = [(0,1),(1,0),(0,-1),(-1,0)]
  i = 0
  sx,sy = cx, cy
  while True:
    dx , dy = directions[i]
    nx, ny = cx+dx , cy +dy
    # 종료 조건(한바퀴 다돌았을때 종료)
    if 0 <= nx <M  and 0 <= ny < N and visited[ny][nx] == 0:
      visited[ny][nx] = grid[cy][cx]
      cx,cy = nx, ny
      if nx == sx and ny == sy:
        break
    else :
      i=i+1
      continue
  return


for _ in range(R):
  visited = [[0]*M for _ in range(N)]
  cycle = (min(N,M))//2
  for i in range(cycle):
    doligo(N,M,grid,i,i)
  grid = [row[:] for row in visited]


#출력 처리
for i in visited:
  print(*i)

# print(visited)
  
# 소요시간 : 30분
