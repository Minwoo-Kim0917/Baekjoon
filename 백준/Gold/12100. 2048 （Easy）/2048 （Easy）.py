import sys
# sys.stdin = open("input.txt",'r')

def transition(mw_map, direction, N):
    new_mw_map = [[0] * N for _ in range(N)]
    
    if direction == 'up':  
        for cx in range(N):
            stack = []
            for cy in range(N):
                if mw_map[cy][cx] != 0:
                    stack.append(mw_map[cy][cx])
            
            idx = 0
            while stack:
                val = stack.pop(0)
                if stack and val == stack[0]:
                    new_mw_map[idx][cx] = val * 2
                    stack.pop(0)
                else:
                    new_mw_map[idx][cx] = val
                idx += 1
    
    elif direction == 'down':  
        for cx in range(N):
            stack = []
            for cy in range(N - 1, -1, -1):
                if mw_map[cy][cx] != 0:
                    stack.append(mw_map[cy][cx])
            
            idx = N - 1
            while stack:
                val = stack.pop(0)
                if stack and val == stack[0]:
                    new_mw_map[idx][cx] = val * 2
                    stack.pop(0)
                else:
                    new_mw_map[idx][cx] = val
                idx -= 1
    
    elif direction == 'left':  
        for cy in range(N):
            stack = []
            for cx in range(N):
                if mw_map[cy][cx] != 0:
                    stack.append(mw_map[cy][cx])
            
            idx = 0
            while stack:
                val = stack.pop(0)
                if stack and val == stack[0]:
                    new_mw_map[cy][idx] = val * 2
                    stack.pop(0)
                else:
                    new_mw_map[cy][idx] = val
                idx += 1
    
    elif direction == 'right':  
        for cy in range(N):
            stack = []
            for cx in range(N - 1, -1, -1):
                if mw_map[cy][cx] != 0:
                    stack.append(mw_map[cy][cx])
            
            idx = N - 1
            while stack:
                val = stack.pop(0)
                if stack and val == stack[0]:
                    new_mw_map[cy][idx] = val * 2
                    stack.pop(0)
                else:
                    new_mw_map[cy][idx] = val
                idx -= 1
    
    return new_mw_map

def dfs(mw_map, degree, N):
    global max_value
    directions = ['up','down','left','right']
    
    if degree == 5:
        max_value = max(max_value, max(map(max, mw_map)))
        return
    
    for direction in directions:
        new_mw_map = transition(mw_map, direction, N)
        # if new_mw_map != mw_map:
        dfs(new_mw_map, degree + 1, N)


N = int(sys.stdin.readline())
mw_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

max_value = 0
dfs(mw_map, 0, N)
print(max_value)
