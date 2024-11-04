"""Ler uma lista de 5 números inteiros e
mostre cada número juntamente com a
sua posição na lista."""
lista =[]
for n in range(5):
    numero = int(input("Digite um numero:"))
    lista.append(numero)
print(lista)
print("Agora vamos falar a indice")
for i, numero in enumerate(lista):
    print("A indice {} = a o numero {}".format(i,numero))
