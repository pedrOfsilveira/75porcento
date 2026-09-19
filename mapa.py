import random as rd

import aroeira as ar
import config
from salas import ROOM_LAYOUTS
from tile import Tile

# ESTADO DA SALA ATUAL (troquei pixel por tile e renderizado por solido)
solidos: list[Tile] = []  # qualquer coisa com colisao
extras: list[Tile] = []  # sem colisao
salas: dict = {}
colunas = 0
linhas = 0


def chave_sala():
    return f"{colunas},{linhas}"


def desenhar_sala(matriz, tela):
    global solidos, extras
    solidos = []
    extras = []

    for linha_i, linha in enumerate(matriz):
        for col, tipo in enumerate(linha):
            if tipo == config.CHAO:
                continue

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


def sala_aleatoria(tela):
    indice = rd.randint(0, len(ROOM_LAYOUTS) - 1)
    desenhar_sala(ROOM_LAYOUTS[indice], tela)


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


def trocar_sala(direcao, tela, player):
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
    if chave in salas:
        solidos, extras = salas[chave]
        _mostrar_sala_atual(tela)
    else:
        sala_aleatoria(tela)

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
