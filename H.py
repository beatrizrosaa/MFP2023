N = int(input())
lista = []*N
lista = list(map(int,input().split()))
ordem = list(map(int,input().split()))
newlist = []


for k in ordem:
    for i in lista:
        for j in lista:
            if i != j:
                if i + j == k:
                    newlist.append(i)
                    newlist.append(j)
                    a = i
                    b = j
                    break
for k in ordem:
  for i in lista: 
    if i + b == k:
      newlist.append(b)
      c = i
      


print(f'{newlist}')