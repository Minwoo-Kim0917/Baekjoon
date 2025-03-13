import sys
input = sys.stdin.readline

N = int(input())  # 배열 크기 입력

A = list(map(int, input().split()))  # 배열 A 입력
B = list(map(int, input().split()))  # 배열 B 입력

A.sort()  # A를 오름차순 정렬
B.sort(reverse=True)  # B를 내림차순 정렬

# 최솟값 S 계산
S = sum(A[i] * B[i] for i in range(N))

print(S)
