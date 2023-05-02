def define_posicoes(linha, coluna, orientacao, tamanho):
    posicao = []
    if orientacao == 'vertical':
        for i in range (tamanho):
            posicao.append([(linha + i),coluna])

    elif orientacao == 'horizontal':
        for i in range(tamanho):
            posicao.append([linha, (coluna + i)])

    return posicao

