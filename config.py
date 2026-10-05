# ESSE ARQUIVO GUARDA TUDO QUE FOR CONSTANTE

TILE = 50
COLUNAS_SALA = 15
LINHAS_SALA = 9

LARGURA_TELA = COLUNAS_SALA * TILE
ALTURA_TELA = LINHAS_SALA * TILE

VELOCIDADE = 5
FPS = 120

TAMANHO_TIRO = 15
VELOCIDADE_TIRO = 4
INTERVALO_ENTRE_TIROS = 15  # 0,25s em 60 fps

VIDAS_INICIAIS = 3
INVENC_FRAMES = 30  # isso aqui da 0,5s de invenc com 60fps, da p mudar

# aqui sao os tipos
CHAO = 0
PAREDE = 1
OBSTACULO = 2
ESPINHO = 3
PORTA = 4
INIMIGO = 5
PORTA_FECHADA = 6
PORTA_BOSS_FECHADA = 7

CORES = {
    PAREDE: "marrom",
    OBSTACULO: "vermelho",
    ESPINHO: "cinza",
    PORTA: "verde",
    PORTA_FECHADA: "vermelho",
    PORTA_BOSS_FECHADA: "laranja",
    INIMIGO: "transparente",
}

TEM_COLISAO = {
    PAREDE: True,
    OBSTACULO: True,
    ESPINHO: False,
    PORTA: False,
    PORTA_FECHADA: True,
    PORTA_BOSS_FECHADA: True,
    INIMIGO: False,
}

# isso aqui sao as coords de onde o player spawna quando sai de cada porta
SPAWN_APOS_PORTA = {
    "cima": (None, 350),
    "baixo": (None, 75),
    "esquerda": (650, None),
    "direita": (75, None),
}
