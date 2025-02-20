# Stack으로 구현해보기
import sys
from collections import deque

input=sys.stdin.readline


stack1 = deque(input().strip())
M = int(input())
stack2 = deque()


for i in range(M):
    command = input().strip()
    if command == 'L':
        if len(stack1) == 0: 
            continue
        else :
            stack2.appendleft(stack1.pop())

    elif command == 'D':
        if len(stack2) ==0:
            continue
        else : 
            stack1.append(stack2.popleft())
        
    elif command == 'B':
        if len(stack1) == 0:
            continue
        else :
            stack1.pop()

    else:
        P_command = command.split()
        stack1.append(P_command[1])

# print(stack1)
# print(stack2)

total_stack = stack1+stack2
print("".join(total_stack))