class Veiculo:

    def __init__ (self, cor, modelo, velocidade, tipo):

        self.ligado = False
        self.cor =  cor 
        self.modelo = modelo
        self.velocidade = velocidade
        self.tipo = tipo

    def liga(self):
        self.ligado = True 

    def desliga(self):
        self.ligado = False

    def acelera(self,velocidade):
        self.velocidade += velocidade 

    def desacelera(self):
        self.velocidade -= 10
    

    def __str__ (self):
        return f'Carro ligado: {self.ligado}, Cor: {self.cor}, Modelo: {self.modelo}, Velocidade: {self.velocidade}'    

class Carro(Veiculo):
        def __init__(self, cor, modelo, velocidade,tipo):
         super().__init__(cor, modelo, velocidade, tipo)
            self.tipo = 4
            self.placa = ''
            self.estacionado = bool

        def estacionar():
            self.estacionado = bool

        def sair_da_vaga():
            self.desocupa = bool   

class Moto(Veiculo):
        def __init__(self, cor, modelo, velocidade,tipo):
            super().__init__(cor, modelo, velocidade, tipo)
            self.tipo = 2
             self.placa = ''
            self.estacionado = bool

        def estacionar():
            self.estacionado = bool

        def sair_da_vaga():
            self.descoupar = bool    

        class Estacionamento():
            def __init__(self):

            self.vagas_de_carros = 5
            self.vagas_de_motos = 5

            self.carro_para_vaga = int
        self.moto_para_vaga = int

        self.total_vagas_livres_carro = 5
        self.total_vagas_livres_moto = 5

        def estacionar_carro():
            self.estacionado = bool

        def estacionar_moto():
            self.estacionado = bool

        def remover_carro():
            self.estacionado = bool        



class Vaga(Estacionamento):
    def __init__(self):
        super().__init__()
        self.id = int
        self.tipo = int 
        self.livre = bool
        self.placa = ''

        def ocupar():
            self.estacionado
        def desocupar():
            self.estacionado   


carro1 = Estacionamento()

carro1.estacionar()







