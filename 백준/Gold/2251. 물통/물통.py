import sys
# sys.stdin = open("C:/Users/SSAFY/Desktop/mwalgo/Algorithm/input.txt", 'r')
input = sys.stdin.readline

import copy
from collections import deque

# 앞에 두개는 비어있고 세번째 물통은 가득 차있음
maxA,maxB,maxC = map(int,input().split())

yonglayng = [maxA,maxB,maxC]

queue = deque()

C_lst = [maxC]
queue.append((0,0,maxC,0))
visited = [(0,0,maxC)]

while queue:
    A,B,C,time = queue.popleft()
    mw_lst = [A,B,C]
    # i는 출발 j 도착
    for i in range(3):
        if mw_lst[i] == 0:
            continue
        for j in range(3):
            #같은것엔 담을 수 없고 , 꽉차있는 곳에 담을 수 없음
            if i == j or mw_lst[j] == yonglayng[j]:
                continue

            #복사
            new_lst = copy.deepcopy(mw_lst)

            # 물통에 옮기기
            namuzi = yonglayng[j] - new_lst[j]
            # 출발지가 더 많음
            if namuzi <= new_lst[i]:
                new_lst[i] -= namuzi
                new_lst[j] = yonglayng[j]
            # 출발지가 더 적음
            else:
                new_lst[j] += new_lst[i]
                new_lst[i] = 0
                
            # a가 0이면 안된다...
            if new_lst[0] == 0 and new_lst[2] not in C_lst:
                C_lst.append(new_lst[2])

            
            #전형적인 BFS
            if (new_lst[0],new_lst[1],new_lst[2]) not in visited:
                visited.append((new_lst[0],new_lst[1],new_lst[2]))
                queue.append((new_lst[0],new_lst[1],new_lst[2],time+1))
            

C_lst.sort()
print(*C_lst)

            

