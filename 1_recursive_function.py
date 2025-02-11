def reverter_caracteres(s):
    if len(s) == 0:
        return s
    else:
        return reverter_caracteres(s[1:]) + s[0]
    
resposta_usr = input("digite uma palavra: ")
print(reverter_caracteres(resposta_usr))
