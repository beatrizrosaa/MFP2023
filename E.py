lista = []
lista = list(map(int,input().split()))
l = 0
for i in lista:
  if i == 1:
    l += 1
    
if i == 1:
  l -= 1
  
if i == 0 and l % 2 != 0:
  print("S")
elif i != 0 and l % 2 == 0:
  print("S")
else:
  print("N?")