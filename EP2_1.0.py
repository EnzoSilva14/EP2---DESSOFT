def define_posicoes(linha, coluna, orientacao, tamanho):
    posicao = []
    if orientacao == 'vertical':
        for i in range (tamanho):
            posicao.append([(linha + i),coluna])

    elif orientacao == 'horizontal':
        for i in range(tamanho):
            posicao.append([linha, (coluna + i)])

    return posicao

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

def faz_jogada (tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posiciona_frota(frota):

    tabuleiro = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
  
    for lista in frota.values():
        for listinha in lista:
          for posicao in listinha:
              tabuleiro[posicao[0]][posicao[1]] = 1

    return tabuleiro

def afundados(frota,tabuleiro):
  navios_afundados = 0
  for lista in frota.values():
          for listinha in lista:
            afundado = True
            for posicao in listinha:
                if tabuleiro[posicao[0]][posicao[1]] != 'X':
                    afundado = False
            if afundado == True:
                navios_afundados += 1

  return navios_afundados