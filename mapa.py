import random as rd

import aroeira as ar
import config
from inimigo import Inimigo
from salas import ROOM_LAYOUTS, BOSS_ROOM

from tile import Tile


# ESTADO DA SALA ATUAL (troquei pixel por tile e renderizado por solido)
lista_inimigos: list[Inimigo] = []
solidos: list[Tile] = []  # qualquer coisa com colisao
extras: list[Tile] = []  # sem colisao
finalizadas: list[bool]
salas: dict = {}
colunas = 0
linhas = 0
coordBoss = ""

def chave_sala():
    return f"{linhas},{colunas}"


def desenhar_sala(matriz, tela, player):
    global solidos, extras, salas
    solidos = []
    extras = []
    contador_de_portas = 0
    #1 = Cima
    #2 = Esquerda
    #3 = Direita
    #4 = Baixo

    for linha_i, linha in enumerate(matriz):
        for col, tipo in enumerate(linha):
            if tipo == config.CHAO:
                continue

            if tipo == config.INIMIGO:
                inimigo = Inimigo(player, col * config.TILE, linha_i * config.TILE)
                tela.adicionar(inimigo.shape)
                lista_inimigos.append(inimigo)
                continue

            if tipo == config.PORTA_FECHADA:
                contador_de_portas += 1
                if contador_de_portas == 1:
                    if f"{linhas - 1},{colunas}" in salas:
                        if f"{linhas - 1},{colunas}" == coordBoss:
                            tipo = config.PORTA_BOSS_FECHADA
                        pass
                    else:
                        tipo = config.PAREDE

                if contador_de_portas == 2:
                    if f"{linhas},{colunas - 1}" in salas:
                        if f"{linhas},{colunas - 1}" == coordBoss:
                            tipo = config.PORTA_BOSS_FECHADA
                        pass
                    else:
                        tipo = config.PAREDE

                if contador_de_portas == 3:
                    if f"{linhas},{colunas + 1}" in salas:
                        if f"{linhas},{colunas + 1}" == coordBoss:
                            tipo = config.PORTA_BOSS_FECHADA
                        pass
                    else:
                        tipo = config.PAREDE

                if contador_de_portas == 4:
                    if f"{linhas + 1},{colunas}" in salas:
                        if f"{linhas + 1},{colunas}" == coordBoss:
                            tipo = config.PORTA_BOSS_FECHADA
                        pass
                    else:
                        tipo = config.PAREDE

            tile = Tile(
                origem=ar.Ponto(col * config.TILE, linha_i * config.TILE),
                cor=config.CORES[tipo],
                colisao=config.TEM_COLISAO[tipo],
                tipo=tipo,
            )
            if tile.colisao:
                solidos.append(tile)
            else:
                extras.append(tile)

            tela.adicionar(tile.shape)
    salas[chave_sala()] = (solidos, extras)



def sala_aleatoria(tela, player):
    indice = rd.randint(0, len(ROOM_LAYOUTS) - 1)
    desenhar_sala(ROOM_LAYOUTS[indice], tela, player)

def sala_boss():
    global coordBoss
    maior = 0
    #salas[coord][0] = Soma das colunas e linhas para saber qual sala é mais longe
    print(salas)

    for coord in salas:
        if int(salas[coord][0]) > int(maior):
            maior = salas[coord][0] 
            coordBoss = coord
    return coordBoss


def remover_mapa(tela, player):
    tela.remover(player.shape)
    for tile in solidos:
        tela.remover(tile.shape)
    for tile in extras:
        tela.remover(tile.shape)


def _mostrar_sala_atual(tela):
    for tile in solidos:
        tela.adicionar(tile.shape)
    for tile in extras:
        tela.adicionar(tile.shape)


def trocar_sala(direcao, tela, player, bossCoordenada):
    global colunas, linhas, solidos, extras
    
    remover_mapa(tela, player)

    if direcao == "cima":
        linhas -= 1
    elif direcao == "baixo":
        linhas += 1
    elif direcao == "direita":
        colunas += 1
    elif direcao == "esquerda":
        colunas -= 1

    chave = chave_sala()

    #Esse len eu utilizei pois estou setando o mapa primeiro sem nada, somente com a key do dicionario.
    
    if chave in salas and len(salas[chave]) > 1:
        solidos, extras = salas[chave]
        _mostrar_sala_atual(tela)

    elif chave == bossCoordenada:
        desenhar_sala(BOSS_ROOM[0], tela, player)

    else:
        sala_aleatoria(tela, player)


    tela.adicionar(player.shape)


def direcao_da_porta(tile: Tile) -> str | None:
    if tile.shape.y <= config.TILE:
        return "cima"
    if tile.shape.y >= config.ALTURA_TELA - config.TILE:
        return "baixo"
    if tile.shape.x <= config.TILE:
        return "esquerda"
    if tile.shape.x >= config.LARGURA_TELA - config.TILE:
        return "direita"
    return None


def finalizar_sala(sala):
    return

def pode_criar_sala():
    # Posição atual
    atual = f"{linhas},{colunas}"
    cima = f"{linhas + 1},{colunas}"
    baixo = f"{linhas - 1},{colunas}"
    direita = f"{linhas},{colunas + 1}"
    esquerda = f"{linhas},{colunas - 1}"

    # Verifica se já existe
    if atual in salas:
        return False

    # Quadrado para cima/direita
    if (cima in salas and
        direita in salas and
        f"{linhas + 1},{colunas + 1}" in salas):
        return False

    # Quadrado para cima/esquerda
    if (cima in salas and
        esquerda in salas and
        f"{linhas + 1},{colunas - 1}" in salas):
        return False

    # Quadrado para baixo/direita
    if (baixo in salas and
        direita in salas and
        f"{linhas - 1},{colunas + 1}" in salas):
        return False

    # Quadrado para baixo/esquerda
    if (baixo in salas and
        esquerda in salas and
        f"{linhas - 1},{colunas - 1}" in salas):
        return False

    return True

ramificacoes = []

def mapa_aleatorio():
    global colunas, linhas, salas, ramificacoes

    direcoes = ["+coluna", "-coluna", "+linha", "-linha"]
    contador = 0
    
    ramificacoes_iniciais()
    #Sala Inicial
    salas[chave_sala()] = [0]

    
    # A sala inicial pode ser usada para criar uma ramificação
    ramificacoes.append((linhas, colunas))

    while contador < 15:
        # 25% de chance de voltar para uma sala anterior
        if len(ramificacoes) > 0:
            chance = rd.randint(0, 3)

            if chance == 0:
                posicao = rd.choice(ramificacoes)

                linhas = posicao[0]
                colunas = posicao[1]

        aleat = rd.randint(0, 3)


        if direcoes[aleat] == "+coluna":
            colunas += 1
            soma = abs(linhas) + abs(colunas)

            if pode_criar_sala():
                salas[chave_sala()] = [soma]
                contador += 1

                # Guarda essa sala como possível ponto de ramificação
                ramificacoes.append((linhas, colunas))

            else:
                colunas -= 1

        elif direcoes[aleat] == "-coluna":
            colunas -= 1
            soma = abs(linhas) + abs(colunas)

            if pode_criar_sala():
                salas[chave_sala()] = [soma]
                contador += 1

                ramificacoes.append((linhas, colunas))

            else:
                colunas += 1

        elif direcoes[aleat] == "+linha":
            linhas += 1
            soma = abs(linhas) + abs(colunas)

            if pode_criar_sala():
                salas[chave_sala()] = [soma]
                contador += 1

                ramificacoes.append((linhas, colunas))

            else:
                linhas -= 1

        elif direcoes[aleat] == "-linha":
            linhas -= 1
            soma = abs(linhas) + abs(colunas)

            if pode_criar_sala():
                salas[chave_sala()] = [soma]
                contador += 1

                ramificacoes.append((linhas, colunas))

            else:
                linhas += 1
    linhas = 0
    colunas = 0

def ramificacoes_iniciais():
    global ramificacoes 
    
    direcoes = ["+coluna", "-coluna", "+linha", "-linha"]
    contador = 0
    quantidade = rd.randint(2,4)

    while contador < quantidade:
        aleat = rd.randint(0,3)

        if direcoes[aleat] == "+coluna":
            posicao = (0,1)

        elif direcoes[aleat] == "-coluna":
            posicao = (0,-1)

        elif direcoes[aleat] == "+linha":
            posicao = (1,0)

        elif direcoes[aleat] == "-linha":
            posicao = (-1,0)

        if posicao not in ramificacoes:
            salas[f"{posicao[0]},{posicao[1]}"] = [abs(posicao[0]) + abs(posicao[1])]
            ramificacoes.append(posicao)
            contador += 1
