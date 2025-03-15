num_N = int(input())
mw_grid = list(map(int, input().split()))

# 빠른 탐색을 위해 set 사용
mw_set = set(mw_grid)

for i in range(2, 1000001):
    find = True
    for A in mw_grid:
        if i % A != 0:  # i가 A의 배수가 아니라면 제외
            find = False
            break
        if i // A not in mw_set:  # i를 A로 나눈 몫이 mw_grid에 없으면 제외
            find = False
            break
    if find:
        print(i)
        break





