from collections import*
I=lambda:[*map(int,input().split())]
n,m=I()
g=[[]for _ in[n]*-~n]
for _ in[m]*m:a,b=I();g[a]+=[b];g[b]+=[a]
k=I()[0]
c=I()
F=1<<k
r,R=range(k),range(F)
G=[k*[F]for _ in r]
for i in r:
 D=[F]*-~n;D[c[i]]=0;q=deque([c[i]])
 while q:
  v=q.popleft()
  for t in g[v]:
   if D[t]>k:D[t]=D[v]+1;q+=[t]
 G[i]=[D[c[j]]for j in r]
p=[k*[F]for _ in R]
for i in r:p[1<<i][i]=1
for b in R:
 for v in r:
  if b>>v&1:
   for u in r:p[b|1<<u][u]=min(p[b|1<<u][u],p[b][v]+G[v][u])
a=min(p[-1])
print([-1,a][a<F])