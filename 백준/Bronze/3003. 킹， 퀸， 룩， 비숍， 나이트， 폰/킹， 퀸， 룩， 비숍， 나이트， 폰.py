

mw_lst = [1,1,2,2,2,8]
new_lst = list(map(int,input().split()))
for i in range(6):
    mw_lst[i] -= new_lst[i]
print(*mw_lst)