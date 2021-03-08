from random import randint
for _ in range(1000):
    n = randint(1, 100)
    m = randint(1, n)
    a = [randint(0, n - 1) for _ in range(n)]


    cnt = [0] * (n + 1)
    for x in a[:m]:
        cnt[x] += 1

    for k in range(m + 1):
        if cnt[k] == 0:
            ans = mex_now = k
            break

    for i, x in enumerate(a[m:]):
        cnt[x] += 1
        if cnt[x] == 1 and mex_now == x:
            for k in range(x + 1, m + 1):
                if not cnt[k]:
                    mex_now = k
                    break

        o = a[i]
        cnt[o] -= 1
        if cnt[o] == 0 and mex_now > o:
            mex_now = o

        ans = min(ans, mex_now)

    print(ans)