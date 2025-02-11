def contar_caracteres(s, c):
    if not s:
        return 0
    return (1 if s[0] == c else 0) + contar_caracteres(s[1:], c)

print(contar_caracteres("banana", "b"))