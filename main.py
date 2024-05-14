def remove_comentario(code):
    bloco_comentario = False
    linhas = code.split('\n')
    resultado = []

    for linha in linhas:
        linha = linha.strip()

        if not bloco_comentario:
            if '//' in linha:
                linha = linha[:linha.index('//')]
            if '/*' in linha:
                if '*/' in linha:
                    linha = linha[:linha.index('/*')] + linha[linha.index('*/')+2:]  #se isso nn funfar eu coringo
                else:
                    bloco_comentario = True
                    linha = linha[:linha.index('/*')]
            if linha:
                resultado.append(linha)
        else:
            if '*/' in linha:
                bloco_comentario = False
                linha = linha[linha.index('*/')+2:]
                if linha:
                    resultado.append(linha)

    return '\n'.join(resultado)

codigo_com_comentarios = []
print("Digite um código fonte com comentário (deixe em branco para finalizar):\n ")
while True:
    linha = input("")
    if not linha:  
        break
    codigo_com_comentarios.append(linha)

codigo_sem_comentarios = remove_comentario('\n'.join(codigo_com_comentarios))
print("\n")
print("_"*50)
print("Resultado: \n\n")

print(codigo_sem_comentarios)
print("\n")
print("_"*50)