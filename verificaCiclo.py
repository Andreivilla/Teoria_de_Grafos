def verificaCiclo(arcos):
    if arcos[0] != arcos[len(arcos)-1]:
        return False
    for i in range(len(arcos)-1):
        for j in range(i+1, len(arcos)-1, +1):
            if(arcos[i] == arcos[j]):
                return False
    return True

print("numero de arcos: ")
nArcos = int(input())
vetArcos = []
for i in range(nArcos):
    vetArcos.append(input())

print(verificaCiclo(vetArcos))