import aroeira as ar
import colisao
import config
import mapa
from inimigo import Inimigo
from player import Player

tela = ar.Tela("Roguelike", config.LARGURA_TELA, config.ALTURA_TELA)
mapa.sala_aleatoria(tela)

player = Player()
inimigo = Inimigo(player)

texto_vidas = ar.Texto(
    ar.Ponto(config.TILE, config.TILE),
    f"Vidas: {player.health}",
    16,
    "preto",
)
tela.adicionar(texto_vidas)
tela.adicionar(player.shape)
tela.adicionar(inimigo.shape)

teclas = set()


def pressionar(nome):
    teclas.add(nome.casefold())

    if nome == "F":
        print(f"Localização: {mapa.colunas},{mapa.linhas}")
        # print(mapa.extras)
        player.dano(texto_vidas)
        print(mapa.salas)


def soltar(nome):
    teclas.discard(nome.casefold())


def atualizar():
    colisao.processar_extras(player, tela, texto_vidas)

    if "w" in teclas:
        player.mover_e_resolver(0, -config.VELOCIDADE, mapa.solidos)
    if "s" in teclas:
        player.mover_e_resolver(0, config.VELOCIDADE, mapa.solidos)
    if "a" in teclas:
        player.mover_e_resolver(-config.VELOCIDADE, 0, mapa.solidos)
    if "d" in teclas:
        player.mover_e_resolver(config.VELOCIDADE, 0, mapa.solidos)


    inimigo.mover_e_resolver(mapa.solidos)
    # mover_inimigo()
    player.tick_invenc()


tela.ao_pressionar_tecla(pressionar)
tela.ao_soltar_tecla(soltar)
tela.animar(atualizar, fps=config.FPS)
tela.executar()
