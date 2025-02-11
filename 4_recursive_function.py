def posicao_maior_elemento(lista):
    if len(lista) == 1:
        return 0
    indice_resto = posicao_maior_elemento(lista[1:]) + 1
    if lista[0] > lista[indice_resto]:
        return 0
    else:
        return indice_resto
    
maior_elemento = ([1, 5, 3, 9, 2]) 
print(posicao_maior_elemento(maior_elemento))