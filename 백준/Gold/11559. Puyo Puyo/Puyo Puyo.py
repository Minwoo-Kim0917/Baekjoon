import sys
from collections import deque
# sys.stdin = open("C:/Users/SSAFY/Desktop/mwalgo/Algorithm/input.txt", 'r')
input = sys.stdin.readline

# 입력처뤼
Bboogrid = [list(input().strip()) for _ in range(12)]

# 방향: 상하좌우
directions = [(1,0),(0,1),(-1,0),(0,-1)]

def pangpang(x, y, visited, color):
    #전형적인 BFS는아니고 visted를 쓰는 BFS
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True
    connected = [(x, y)]
    
    while queue:
        cx, cy = queue.popleft()
        #파이썬만 가능한 언팩크
        for dx,dy in directions:
            nx, ny = cx + dx, cy + dy
            # 방문하지 않은곳만 방문하기
            if 0 <= nx < 6 and 0 <= ny < 12 and not visited[ny][nx] and Bboogrid[ny][nx] == color:
                visited[ny][nx] = True
                queue.append((nx, ny))
                connected.append((nx, ny))
    
    return connected

# 팡한다음 밑으로내리기
def drop():
    #2048 문제와 매우비슷?
    for x in range(6):
        stack = deque()
        for y in range(11, -1, -1):
            if Bboogrid[y][x] != '.':
                stack.append(Bboogrid[y][x])
        for y in range(11, -1, -1):
            if stack:
                Bboogrid[y][x] = stack.popleft()
            else:
                Bboogrid[y][x] = '.'

# 연쇄 횟수
cnt = 0

#될때까지 반복
while True:
    #visted 초기화(새로운 그리드이무로)
    visited = [[False] * 6 for _ in range(12)]
    #터트려야할 좌표들을 모으기
    should_pang = []

    for y in range(12):
        for x in range(6):
            if Bboogrid[y][x] != '.' and not visited[y][x]:
                #터트려야할 좌표들 저장
                result = pangpang(x, y, visited, Bboogrid[y][x])
                if len(result) >= 4:
                    should_pang.extend(result)
            
    #팡할거 없으면 --> 이제 그만할떄 됏다
    if not should_pang:
        break
    # 팡해야할곳을 다 .으로 바꿔준다
    for x, y in should_pang:
        Bboogrid[y][x] = '.'
    # 떨궈
    drop()
    #개수세
    cnt += 1

print(cnt)

  
    
