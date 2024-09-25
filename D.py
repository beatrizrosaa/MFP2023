M1, M2 = map(float,input().split())
X1, X2 = map(float,input().split())
F = float(input())
d = X2 - X1
p1 = M1* M2
p2 = (d**2) * F
G = p2 / p1
print(round(G,10))