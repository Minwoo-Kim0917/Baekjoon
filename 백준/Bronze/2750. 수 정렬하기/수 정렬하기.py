N = int(input())
N_lst = []
for _ in range(N):
    N_lst.append(int(input()))

N_lst.sort()
for k in range(N):
    print(N_lst[k])