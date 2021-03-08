from random import sample, choice

def verify(ans, s1, s2, s3, n):
    s1 *= 2
    s2 *= 2
    s3 *= 2
    i1 = i2 = i3 = 0
    for l1, l2, l3 in zip(s1, s2, s3):
        if i1 < 2 * n + 1 and ans[i1] == l1:
            i1 += 1
        if i2 < 2 * n + 1 and ans[i2] == l2:
            i2 += 1
        if i3 < 2 * n + 1 and ans[i3] == l3:
            i3 += 1

    return i1 == i2 == i3 == 2 * n + 1

def solve():
    n = int(input())
    s1 = input()
    s2 = input()
    s3 = input()

    ans = ("0" * n + "1" + "0" * n)
    if not verify(ans, s1, s2, s3, n):
        ans = ("1" * n + "0" + "1" * n)
        if not verify(ans, s1, s2, s3, n):
            ans1 = "1" + "0" * (n - 1)
            ans = ans1 + "0" + ans1
            if not verify(ans, s1, s2, s3, n):
                ans1 = "1" + "0" * (n - 1)
                ans = ans1 + "1" + ans1
                if not verify(ans, s1, s2, s3, n):
                    ans1 = "1" * (n - 1) + "0"
                    ans = ans1 + "0" + ans1
                    if not verify(ans, s1, s2, s3, n):
                        ans1 = "1" * (n - 1) + "0"
                        ans = ans1 + "1" + ans1
                        if not verify(ans, s1, s2, s3, n):
                            ans = s1 + s1[0]
                            if not verify(ans, s1, s2, s3, n):
                                ans = s2 + s2[0]
                                if not verify(ans, s1, s2, s3, n):
                                    ans = s3 + s3[0]
                                    if not verify(ans, s1, s2, s3, n):
                                        ans1 = "1" * (n - 2) + "0" + "1"
                                        ans = ans1 + "0" + ans1
                                        if not verify(ans, s1, s2, s3, n):
                                            ans = ""
    if ans == "":
        ans1 = "0" + "1" * (n - 1)
        ans = ans1 + "1" + ans1
        if not verify(ans, s1, s2, s3, n):
            ans1 = "0" + "1" * (n - 1)
            ans = ans1 + "0" + ans1
            if not verify(ans, s1, s2, s3, n):
                ans1 = "0" * (n - 1) + "1"
                ans = ans1 + "1" + ans1
                if not verify(ans, s1, s2, s3, n):
                    ans1 = "0" * (n - 1) + "1"
                    ans = ans1 + "0" + ans1
                    if not verify(ans, s1, s2, s3, n):
                        ans1 = "1" * (n - 2) + "01"
                        ans = ans1 + "0" + ans1
                        if not verify(ans, s1, s2, s3, n):
                            ans1 = "1" * (n - 2) + "01"
                            ans = ans1 + "1" + ans1
                            if not verify(ans, s1, s2, s3, n):
                                ans1 = "0" * (n - 2) + "10"
                                ans = ans1 + "0" + ans1
                                if not verify(ans, s1, s2, s3, n):
                                    ans1 = "0" * (n - 2) + "10"
                                    ans = ans1 + "1" + ans1
                                    if not verify(ans, s1, s2, s3, n):
                                        ans = ""
    if ans == "":
        ans1 = "10" + "1" * (n - 2)
        ans = ans1 + "1" + ans1
        if not verify(ans, s1, s2, s3, n):
            ans1 = "10" + "1" * (n - 2)
            ans = ans1 + "0" + ans1
            if not verify(ans, s1, s2, s3, n):
                ans1 = "01" + "0" * (n - 2)
                ans = ans1 + "1" + ans1
                if not verify(ans, s1, s2, s3, n):
                    ans1 = "01" + "0" * (n - 2)
                    ans = ans1 + "0" + ans1
                    while not verify(ans, s1, s2, s3, n):
                        ans = "".join(s1[i] for i in sorted(sample(range(2 * n), k=n)))
                        ans = ans + choice("01") + ans
    
    print(ans)

t = int(input())
for _ in range(t):
    solve()