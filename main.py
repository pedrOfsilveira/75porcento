import aroeira as ar
import colisao
import config
import mapa
from player import Player
from tiro import Tiros

tela = ar.Tela("Roguelike", config.LARGURA_TELA, config.ALTURA_TELA)
player = Player()
finalizada = False
mapa.mapa_aleatorio()
coordBoss = mapa.sala_boss()
mapa.sala_aleatoria(tela, player)

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
        print(f"Localização: {mapa.linhas},{mapa.colunas}")
        player.dano(texto_vidas)
        print(f"coordenada do boss: {coordBoss}")
    

def soltar(nome):
    teclas.discard(nome.casefold())

def atualizar():
    global finalizada
    finalizada = False
    sala_atual = mapa.chave_sala()
    colisao.processar_extras(player, tela, texto_vidas, coordBoss)

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

    tiros.atualizar(mapa.solidos, teclas)

    if len(mapa.lista_inimigos) >= 1:
        finalizada = False
        for inimigo in mapa.lista_inimigos.copy():
            if inimigo.health == 0:
                tela.remover(inimigo.shape)
                mapa.lista_inimigos.remove(inimigo)

            inimigo.mover_e_resolver(mapa.solidos)
            tiros.atualizar_com_inimigo(inimigo)
            player.tick_invenc()

    if len(mapa.lista_inimigos) == 0 and finalizada == False:

        if finalizada == False:

            for bloquinho in mapa.solidos.copy():
                
                if bloquinho.tipo == config.PORTA_FECHADA:
                    bloquinho.tipo = config.PORTA
                    bloquinho.colisao = config.TEM_COLISAO[bloquinho.tipo]
                    bloquinho.shape.cor = config.CORES[bloquinho.tipo]
                    mapa.solidos.remove(bloquinho)
                    mapa.extras.append(bloquinho)
                    
                elif bloquinho.tipo == config.PORTA_BOSS_FECHADA:
                    bloquinho.tipo = config.PORTA
                    bloquinho.colisao = config.TEM_COLISAO[bloquinho.tipo]
                    bloquinho.shape.cor = "laranja"
                    mapa.solidos.remove(bloquinho)
                    mapa.extras.append(bloquinho)
            



tela.ao_pressionar_tecla(pressionar)
tela.ao_soltar_tecla(soltar)
tela.animar(atualizar, fps=config.FPS)
tela.executar()
