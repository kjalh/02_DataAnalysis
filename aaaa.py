import sys
input = sys.stdin.readline

def solution():
    a = list(map(int, input().split()))
    print((a[0] and a[1]) or (a[2] and a[3]))

solution()

