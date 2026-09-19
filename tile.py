import aroeira as ar

import config


class Tile:
    """Um quadrado do mapa (parede, espinho, porta, etc.)."""

    def __init__(self, origem: ar.Ponto, cor: str, colisao: bool, tipo: int):
        self.shape = ar.Retangulo(
            altura=config.TILE, largura=config.TILE, origem=origem, cor=cor
        )
        self.colisao = colisao
        self.tipo = tipo
