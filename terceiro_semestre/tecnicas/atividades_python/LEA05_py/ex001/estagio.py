def correcao(string):
    corrigida = ''.join(sorted(set(string)))
    if string.endswith(corrigida):
        string_original = string[:len(string) - len(corrigida)]
    else:
        string_original = string
    return corrigida

string = input()
resultado = correcao(string)
print(resultado)
