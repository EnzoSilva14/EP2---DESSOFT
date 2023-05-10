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

def posicao_valida(frota, linha, coluna, orientacao, tamanho):

    posicao = define_posicoes(linha, coluna, orientacao, tamanho)

    for par in posicao:
        if par[0] > 9 or par[1] > 9:
            return False
        for lista in frota.values():
            for listinha in lista:
                if par in listinha:
                    return False
    return True

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

dicio = {
    "porta-aviões": [4],
    "navio-tanque": [3,3],
    "contratorpedeiro": [2,2,2],
    "submarino": [1,1,1,1],

}

for navio in dicio:
    for i in range(len(dicio[navio])):
        tamanho = dicio[navio][i]
        print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(navio, tamanho))
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        if tamanho > 1:
            oriente = int(input('[1] Vertical [2] Horizontal >'))
            if oriente == 1:
                orientacao = 'vertical'
            else:
                orientacao = 'horizontal'

        valida = False
        while valida == False:
            
            valida = posicao_valida(frota, linha, coluna, orientacao, tamanho)
            if valida == True:
                posicao = define_posicoes(linha, coluna, orientacao, tamanho)
                frota[navio].append(posicao)
        
            else:
                print('Esta posição não está válida!')
                print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(navio, tamanho))
                linha = int(input('Linha: '))
                coluna = int(input('Coluna: '))
                if tamanho > 1:
                    oriente = int(input('[1] Vertical [2] Horizontal >'))
                    if oriente == 1:
                        orientacao = 'vertical'
                    else:
                        orientacao = 'horizontal'                
    
print (frota)