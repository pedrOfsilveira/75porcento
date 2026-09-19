import aroeira as ar
import config


class Player:
    def __init__(self):
        self.shape = ar.Retangulo(
            origem=ar.Ponto(x=7 * config.TILE, y=config.TILE + 25),
            largura=25,
            altura=25,
            cor="roxo",
        )
        self.health = config.VIDAS_INICIAIS
        self.invenc = 0

    def tocando(self, outro) -> bool:
        # colisao entre o jogador e um objeto com shape
        a = self.shape
        b = outro.shape
        return (
            a.x < b.x + b.largura
            and a.x + a.largura > b.x
            and a.y < b.y + b.altura
            and a.y + a.altura > b.y
        )

    def dano(self, texto_vidas):
        if self.invenc == 0:
            self.health -= 1
            self.invenc = config.INVENC_FRAMES
            texto_vidas.conteudo = f"Vidas: {self.health}"

    def tick_invenc(self):
        if self.invenc > 0:
            self.invenc -= 1

    def mover_e_resolver(self, dx, dy, solidos):
        # move e empurra de volta se for solido.
        # isso aqui tava no atualizar na main
        # mas resolvi separar
        if dx != 0:
            self.shape.mover(dx=dx)
            bloco = self._primeiro_solido(solidos)
            if bloco is not None:
                if dx > 0:
                    self.shape.mover(
                        dx=(bloco.shape.x - self.shape.largura) - self.shape.x
                    )
                else:
                    self.shape.mover(
                        dx=(bloco.shape.x + bloco.shape.largura) - self.shape.x
                    )

        if dy != 0:
            self.shape.mover(dy=dy)
            bloco = self._primeiro_solido(solidos)
            if bloco is not None:
                if dy > 0:
                    self.shape.mover(
                        dy=(bloco.shape.y - self.shape.altura) - self.shape.y
                    )
                else:
                    self.shape.mover(
                        dy=(bloco.shape.y + bloco.shape.altura) - self.shape.y
                    )

    def _primeiro_solido(self, solidos):
        for bloco in solidos:
            if self.tocando(bloco):
                return bloco
        return None
