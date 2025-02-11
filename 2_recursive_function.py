def soma_lista_aninhada(n):
    if not n:
        return 0
    first = n[0]
    if isinstance(first, list):
        soma_primeiro = soma_lista_aninhada(first)
    else:
        soma_primeiro = first
    return soma_primeiro + soma_lista_aninhada(n[1:])

lista_numeros = ([1, [2, 9], [4, [5]]])

print(soma_lista_aninhada(lista_numeros))