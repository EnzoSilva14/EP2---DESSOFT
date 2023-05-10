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
    
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}
tabuleiro_inimigo = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)
lista_posicoes = list()

jogando = True
while jogando == True:
    def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
        texto = ''
        texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
        texto += '_______________________________      _______________________________\n'

        for linha in range(len(tabuleiro_jogador)):
            jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
            oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
            texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
        return texto

    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_inimigo))
    verifica = False
    while verifica == False:
        linha_ataque = int(input('Jogador, qual linha deseja atacar? '))
        while linha_ataque > 9 or linha_ataque < 0:
            print('Linha inválida!')
            linha_ataque = int(input('Jogador, qual linha deseja atacar? '))

        coluna_ataque = int(input('Jogador, qual coluna deseja atacar? '))
        while coluna_ataque > 9 or coluna_ataque < 0:
            print('Coluna inválida!')
            coluna_ataque = int(input('Jogador, qual coluna deseja atacar? '))

        posicao_ataque = [linha_ataque, coluna_ataque]
        if posicao_ataque in lista_posicoes:
            print('A posição linha {0} e coluna {1} já foi informada anteriormente!'.format(linha_ataque, coluna_ataque))
        else:
            verifica = True
            lista_posicoes.append(posicao_ataque)
            tabuleiro_inimigo = faz_jogada(tabuleiro_inimigo, linha_ataque, coluna_ataque)  
            afundou = afundados(frota_oponente,tabuleiro_inimigo)

        if afundou == 10:
            print('Parabéns! Você derrubou todos os navios do seu oponente!')
            jogando = False
        
    
