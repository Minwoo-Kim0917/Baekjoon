def max_val(N, K, mw_lst):
    burger_lst = [i for i in range(N) if mw_lst[i] == 'H']
    people_lst = [i for i in range(N) if mw_lst[i] == 'P']
    
    h_idx, p_idx = 0, 0
    eaten = 0

    while p_idx < len(people_lst) and h_idx < len(burger_lst):
        person = people_lst[p_idx]  
        burger = burger_lst[h_idx]
        
        if abs(person - burger) <= K:
            eaten += 1
            p_idx += 1
            h_idx += 1
        elif burger < person - K:
            h_idx += 1
        else:
            p_idx += 1

    return eaten

N,K = map(int,input().split())
mw_lst = input()
print(max_val(N, K, mw_lst))  