def preenche_frota (frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicao = []
    if orientacao == 'vertical':
        for i in range (tamanho):
            posicao.append([(linha + i),coluna])

    elif orientacao == 'horizontal':
        for i in range(tamanho):
            posicao.append([linha, (coluna + i)])
    if nome_navio not in frota:
        frota[nome_navio] = [posicao]
    else:
        frota[nome_navio].append(posicao)
    return frota
frota = {}
nome_navio = 'navio-tanque'
linha = 6
coluna = 1
orientacao = 'horizontal'
tamanho = 3

resultado = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
print(resultado)

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro