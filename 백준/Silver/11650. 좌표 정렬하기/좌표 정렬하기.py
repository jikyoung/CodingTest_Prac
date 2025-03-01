import sys
input = sys.stdin.readline

n = int(input())
pair = []

for _ in range(n):
    a,b = map(int, input().split())
    pair.append((a,b))

pair.sort(key=lambda x:(x[0],x[1]))

for a, b in pair:
    print(a,b)
