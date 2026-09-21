import aroeira as ar
import colisao
import config
import mapa
from inimigo import Inimigo
from player import Player
from tiro import Tiros

tela = ar.Tela("Roguelike", config.LARGURA_TELA, config.ALTURA_TELA)
mapa.sala_aleatoria(tela)

lista_inimigos: list[Inimigo] = []
player = Player()
tiros = Tiros(tela, player)

texto_vidas = ar.Texto(
    ar.Ponto(config.TILE, config.TILE),
    f"Vidas: {player.health}",
    16,
    "preto",
)
tela.adicionar(texto_vidas)
tela.adicionar(player.shape)


teclas = set()


def pressionar(nome):
    teclas.add(nome.casefold())

    tiros.atirar(nome)

    if nome == "F":
        inimigo = Inimigo(player)
        print(f"Localização: {mapa.colunas},{mapa.linhas}")
        tela.adicionar(inimigo.shape)
        lista_inimigos.append(inimigo)
        inimigo = ''


def soltar(nome):
    teclas.discard(nome.casefold())

def atualizar():
    sala_atual = mapa.chave_sala()

    if mapa.chave_sala() != sala_atual:
        tiros.limpar()

    if "w" in teclas:
        player.mover_e_resolver(0, -config.VELOCIDADE, mapa.solidos)
    if "s" in teclas:
        player.mover_e_resolver(0, config.VELOCIDADE, mapa.solidos)
    if "a" in teclas:
        player.mover_e_resolver(-config.VELOCIDADE, 0, mapa.solidos)
    if "d" in teclas:
        player.mover_e_resolver(config.VELOCIDADE, 0, mapa.solidos)

    for inimigoatual in lista_inimigos:

        colisao.processar_extras(player, inimigoatual, tela, texto_vidas)
        tiros.atualizar(mapa.solidos, inimigoatual, teclas)
        inimigoatual.mover_e_resolver(mapa.solidos)
        
        if inimigoatual.health == 0:
            tela.remover(inimigoatual.shape)

    player.tick_invenc()


tela.ao_pressionar_tecla(pressionar)
tela.ao_soltar_tecla(soltar)
tela.animar(atualizar, fps=config.FPS)
tela.executar()
