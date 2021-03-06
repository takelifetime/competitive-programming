from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import combinations, permutations
from math import gcd, sin, cos, tan, degrees, radians
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = float("inf")

n, k = map(int, input().split())
h = list(map(int, input().split()))

h.sort()

if k != 0:
    h = h[:-k]

print(sum(h))