# ESSE ARQUIVO É ESPECIFICAMENTE PRA COLSIAO

import config
import mapa

trocando_sala = False


def processar_extras(player, tela, texto_vidas, bossCoordenada):
    global trocando_sala

    tocando_porta = False

    for tile in mapa.extras:
        if not player.tocando(tile):
            continue

        if player.tocando(tile) and tile.tipo == config.ESPINHO:
            player.dano(texto_vidas)


        if tile.tipo == config.PORTA:
            tocando_porta = True

            if trocando_sala:
                continue

            direcao = mapa.direcao_da_porta(tile)
            if direcao is None:
                continue

            trocando_sala = True
            mapa.trocar_sala(direcao, tela, player, bossCoordenada)

            novo_x, novo_y = config.SPAWN_APOS_PORTA[direcao]
            if novo_x is not None:
                player.shape.x = novo_x
            if novo_y is not None:
                player.shape.y = novo_y

            break

    if not tocando_porta:
        trocando_sala = False

def processar_extras_inimigo(inimigo, texto_vidas):
    global trocando_sala

    for tile in mapa.extras:
        if not inimigo.tocando(tile):
            continue

        if inimigo.tocando(tile) and tile.tipo == config.ESPINHO:
            inimigo.dano(texto_vidas)
