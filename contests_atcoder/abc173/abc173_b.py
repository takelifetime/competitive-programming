from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import combinations, permutations
from math import gcd, sin, cos, tan, degrees, radians
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = float("inf")

n = int(input())

s = [input() for _ in range(n)]

c = Counter(s)

for res in ["AC", "WA", "TLE", "RE"]:
    print(f"{res} x {c[res]}")