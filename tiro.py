import aroeira as ar
import config


class Tiro:
    def __init__(self, origem, dx, dy):
        self.shape = ar.Retangulo(
            origem=ar.Ponto(x=origem.x, y=origem.y),
            largura=config.TAMANHO_TIRO,
            altura=config.TAMANHO_TIRO,
            cor="vermelho",
        )
        self.dx = dx
        self.dy = dy

    def mover(self):
        self.shape.mover(dx=self.dx, dy=self.dy)

    def fora_da_tela(self) -> bool:
        return (
            self.shape.x + self.shape.largura < 0
            or self.shape.x > config.LARGURA_TELA
            or self.shape.y + self.shape.altura < 0
            or self.shape.y > config.ALTURA_TELA
        )

    def tocando(self, outro) -> bool:
        a = self.shape
        b = outro.shape
        return (
            a.x < b.x + b.largura
            and a.x + a.largura > b.x
            and a.y < b.y + b.altura
            and a.y + a.altura > b.y
        )


class Tiros:

    def __init__(self, tela, player):
        self.DIRECOES = {
            "arrow up": (0, -config.VELOCIDADE_TIRO),
            "arrow down": (0, config.VELOCIDADE_TIRO),
            "arrow left": (-config.VELOCIDADE_TIRO, 0),
            "arrow right": (config.VELOCIDADE_TIRO, 0),
        }

        self.tela = tela
        self.player = player
        self.ativos: list[Tiro] = []
        self.tempo_ate_atirar = 0

    def atirar(self, tecla):
        if self.tempo_ate_atirar > 0:
            return

        direcao = self.DIRECOES.get(tecla.casefold())
        if direcao is None:
            return

        x = self.player.shape.origem.x + self.player.shape.largura / 2 - config.TAMANHO_TIRO / 2
        y = self.player.shape.origem.y + self.player.shape.altura / 2 - config.TAMANHO_TIRO / 2
        ponto = ar.Ponto(x=x, y=y)
        tiro = Tiro(ponto, dx=direcao[0], dy=direcao[1])
        self.ativos.append(tiro)
        self.tela.adicionar(tiro.shape)
        self.tempo_ate_atirar = config.INTERVALO_ENTRE_TIROS

    def atualizar(self, solidos, inimigo, teclas):
        if self.tempo_ate_atirar > 0:
            self.tempo_ate_atirar -= 1

        if self.tempo_ate_atirar == 0:
            for tecla in self.DIRECOES:
                if tecla in teclas:
                    self.atirar(tecla)
                    break

        for tiro in self.ativos.copy():
            tiro.mover()

            acertou_solido = any(tiro.tocando(bloco) for bloco in solidos)
            acertou_inimigo = inimigo.health > 0 and tiro.tocando(inimigo)

            if tiro.fora_da_tela() or acertou_solido or acertou_inimigo:
                if acertou_inimigo:
                    inimigo.dano()
                self.remover(tiro)

    def remover(self, tiro):
        if tiro in self.ativos:
            self.ativos.remove(tiro)
            self.tela.remover(tiro.shape)

    def limpar(self):
        for tiro in self.ativos.copy():
            self.remover(tiro)
