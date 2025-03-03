N = int(input())

mw_map = list(map(int,input().split()))

M = int(input()) #학생수0
mw_command = []
for _ in range(M):
    mw_command.append(list(map(int,(input().split()))))

for each_command in mw_command :
    #남자 (배수)
    if each_command[0] == 1 :
        for i in range(0,N//each_command[1]):
            idx1 = each_command[1]*(i+1)-1
            mw_map[idx1] = (mw_map[idx1]+1)%2

    # 여자 (대칭)
    if each_command[0] == 2 :
        delta = 1
        idx = each_command[1]-1
        mw_map[idx] = (mw_map[idx]+1)%2
        while idx-delta >= 0 and idx+delta < N:
            if mw_map[idx-delta] == mw_map[idx+delta] :
                mw_map[idx-delta] = (mw_map[idx-delta]+1)%2
                mw_map[idx+delta] = (mw_map[idx+delta]+1)%2
                delta += 1
            else :
                break 

x = 1
for i in range(len(mw_map)):
    if i == 20*x -1 :
        x += 1
        print(mw_map[i])
    else : 
        print(mw_map[i], end = " ")

                
                
