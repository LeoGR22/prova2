def listaVazia(tamanho):
    lista = [0] * tamanho
    return lista

lista1 = listaVazia(int(input("digite o tamanho da lista ")))
listafinal = []

for i in lista1:
    listanova = int(input("preenhca a lista"))
    listafinal.append(listanova)
listaordenada = sorted(listafinal)

print(listafinal)
print(listaordenada)
print(max(listafinal))









