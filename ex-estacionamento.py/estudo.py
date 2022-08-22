
import uuid

class Veiculo:

    def __init__ (self, cor, modelo, tipo, placa, rodas):

        self.cor =  cor 
        self.modelo = modelo
        self._tipo = tipo
        self._rodas = rodas
        self.placa = placa

        @property
        def rodas(self):
            return self._rodas
        
        @rodas.setter
        def rodas(self, value):
            if value == 4:
                return self._tipo == value.replace('carro')
               

                      
#v = Veiculo('azul', 'ford', '4', 'PJK4555')
#print('Cor: {} \n Modelo: {} \n Tipo: {} \n Placa: {}'.format(v.cor, v.modelo, v.tipo, v.placa))

class Carro(Veiculo):

    def __init__(self, cor, modelo, tipo, placa, rodas, estacionado):
        super().__init__(cor, modelo, tipo, placa, rodas)
        self.estacionado = estacionado
        self._rodas = rodas
        self._tipo = tipo  

    def estacionar(self):
        self.estacionado = True  
    def sair_da_vaga(self):
        self.estacionado = False    
 
#car = Carro('azul', 'ford', '4', 'PJH4555', True)
#print('cor: {} \n modelo: {} \n tipo: {} \n placa: {} \n estacionado: {}'.format(car.cor, car.modelo, car.tipo, car.placa, car.estacionado))

class Moto(Veiculo):

    def __init__(self, cor, modelo, tipo, placa, rodas, estacionado):
        super().__init__(cor, modelo, tipo, placa, rodas)
        self.estacionado = estacionado
        self._rodas = rodas
        self._tipo = tipo

    def estacionar(self):
        self.estacionado = True
    def sair_da_vaga(self):
        self.estacionado = False       

#moto = Moto('preta', 'xtr', 'moto', 'PJK4555', False)
#print('cor: {} \n modelo: {} \n tipo: {} \n placa: {} \n estacionado: {}'.format(moto.cor, moto.modelo, moto.tipo, moto.placa, moto.estacionado))       


class Estacionamento:

    def __init__(self, total_vagas, vagas_de_carros, vagas_de_motos, carro_para_vaga, moto_para_vaga, total_vagas_livres_carro, total_vagas_livres_moto):
        

        self.total_vagas = total_vagas

        self.vagas_de_carros = vagas_de_carros
        self.vagas_de_motos = vagas_de_motos

        self.carro_para_vaga = carro_para_vaga
        self.moto_para_vaga = moto_para_vaga

        self.total_vagas_livres_carro = total_vagas_livres_carro
        self.total_vagas_livres_moto = total_vagas_livres_moto

        self.lista_vagas = len

    def estacionar_carro (self):
            self.vagas_de_carros -=1 
            self.total_vagas_livres_carro -=1  
            

    def estacionar_moto (self):
            self.vagas_de_motos -= 1
            self.total_vagas_livres_moto -=1
            
   
    def remover_carro (self):
            self.vagas_de_carros +=1
            self.total_vagas_livres_carro +=1
           

    def remover_moto(self):
            self.vagas_de_motos +=1
            self.total_vagas_livres_moto += 1

    def listar_vagas(self):
        self.lista_vagas = (self.total_vagas_livres_carro + self.total_vagas_livres_moto)        
           


class Vaga():

        def __init__(self, placa, id, livre):
           

            self.placa = placa
            self.id =  id
            self.livre = livre

        def ocupar (self):
         self.total_vagas -=1
   
            
        def desocupar(self):
            self.total_vagas +=1
      
            
#va = Vaga('azul', 'ford', 'carro','PJH4555', uuid.uuid4(), True)
#print('cor: {} \n modelo: {} \n tipo: {} \n placa: {} \n id: {} \n livre: {} '.format(va.cor, va.modelo, va.tipo, va.placa, va.id, va.livre))     


car1 = Carro('azul', 'ford', '','PJH4555', 4, True)
e = Estacionamento(10, 5, 5, 1, 1, 5, 5 )
e.estacionar_carro()
car1.estacionar()
va = Vaga('PJH4555', uuid.uuid4(), True)
e.listar_vagas()



print('----------------------------')
print('Total vagas: {} \n Vagas de carros: {} \n Vagas de motos: {} \n Carro para vaga: {} \n Moto para vaga: {} \n Total vagas livres carro: {} \n Total vagas livres moto: {}'.format (e.total_vagas, e.vagas_de_carros, e.vagas_de_motos, e.carro_para_vaga, e.moto_para_vaga, e.total_vagas_livres_carro, e.total_vagas_livres_moto))   
print('----------------------------')
print('cor: {} \n modelo: {} \n tipo: {} \n placa: {} \n rodas: {} \n estacionado:{}'.format(car1.cor, car1.modelo, car1._tipo, car1.placa, car1._rodas, car1.estacionado))
print('----------------------------')
print('placa:{} \n id: {} \n livre {}'.format(va.placa, va.id, va.livre))
print('----------------------------')
print('O carro tipo está estacionado: {}'.format(car1.estacionado))
print('----------------------------')
print('Liste as vagas: {}'.format(e.lista_vagas))
print('----------------------------')
print('Qual o tipo do carro?{}'.format(car1._tipo))
print('----------------------------')



  