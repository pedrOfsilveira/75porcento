import math

import aroeira as ar
import config
from player import Player
from tile import Tile


class Inimigo:
    def __init__(self, player: Player):
        self.shape = ar.Retangulo(
            origem=ar.Ponto(x=2 * config.TILE, y=2 * config.TILE + 25),
            largura=25,
            altura=25,
            cor="vermelho",
        )
        self.player = player
        self.v = 2
        self._desvio_y = 0
        self._desvio_x = 0

        self.health = config.VIDAS_INICIAIS
        self.invenc = 0


    def dano(self):
        if self.invenc == 0:
           self.health -= 1
           self.invenc = config.INVENC_FRAMES

    def tick_invenc(self):
        if self.invenc > 0:
           self.invenc -= 1

    def mover_inimigo(self):
        dx = self.player.shape.x - self.shape.x
        dy = self.player.shape.y - self.shape.y
        d = math.sqrt(dx**2 + dy**2)

        if d > 0:
            return (dx / d) * self.v, (dy / d) * self.v
        return 0.0, 0.0

    def tocando(self, outro) -> bool:
        a = self.shape
        b = outro.shape
        return (
            a.x < b.x + b.largura
            and a.x + a.largura > b.x
            and a.y < b.y + b.altura
            and a.y + a.altura > b.y
        )

    def mover_e_resolver(self, solidos):
        vx, vy = self.mover_inimigo()

        bloqueou_x, bloco_x = self._mover_eixo(vx, 0, solidos)

        if bloqueou_x:
            if self._desvio_y == 0:
                self._desvio_y = self._escolher_desvio_y(bloco_x)
            self._mover_eixo(0, self._desvio_y * self.v, solidos)
        else:
            self._desvio_y = 0
            bloqueou_y, bloco_y = self._mover_eixo(0, vy, solidos)

            if bloqueou_y:
                if self._desvio_x == 0:
                    self._desvio_x = self._escolher_desvio_x(bloco_y)
                self._mover_eixo(self._desvio_x * self.v, 0, solidos)
            else:
                self._desvio_x = 0

    def _mover_eixo(self, dx, dy, solidos):
        if dx == 0 and dy == 0:
            return False, None

        self.shape.mover(dx=dx, dy=dy)
        bloco = self._primeiro_solido(solidos)
        if bloco is None:
            return False, None

        if dx > 0:
            self.shape.mover(dx=(bloco.shape.x - self.shape.largura) - self.shape.x)
        elif dx < 0:
            self.shape.mover(dx=(bloco.shape.x + bloco.shape.largura) - self.shape.x)

        if dy > 0:
            self.shape.mover(dy=(bloco.shape.y - self.shape.altura) - self.shape.y)
        elif dy < 0:
            self.shape.mover(dy=(bloco.shape.y + bloco.shape.altura) - self.shape.y)

        return True, bloco

    def _escolher_desvio_y(self, bloco):
        py = self.player.shape.y
        ey = self.shape.y
        if abs(py - ey) > 1:
            return 1 if py > ey else -1

        limpar_cima = self.shape.y - (bloco.shape.y - self.shape.altura)
        limpar_baixo = (bloco.shape.y + bloco.shape.altura) - self.shape.y
        return -1 if limpar_cima <= limpar_baixo else 1

    def _escolher_desvio_x(self, bloco):
        px = self.player.shape.x
        ex = self.shape.x
        if abs(px - ex) > 1:
            return 1 if px > ex else -1

        limpar_esq = self.shape.x - (bloco.shape.x - self.shape.largura)
        limpar_dir = (bloco.shape.x + bloco.shape.largura) - self.shape.x
        return -1 if limpar_esq <= limpar_dir else 1

    def _primeiro_solido(self, solidos: list[Tile]):
        for bloco in solidos:
            if self.tocando(bloco):
                return bloco
        return None
