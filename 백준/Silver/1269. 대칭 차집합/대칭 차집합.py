import sys

n, m = map(int, sys.stdin.readline().split())

A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))

sym_diff = A ^ B


print(len(sym_diff))