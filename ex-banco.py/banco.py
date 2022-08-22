#class Cliente:

    #def __init__(self, nome, telefone, renda_mensal, genero):

        #self.nome = nome
        #self.telefone = telefone
        #self.renda_mensal = renda_mensal
        #self.genero = genero

class ContaCorrente:

    def __init__(self):
        self._deposito = 0
        self._saque = 0


        @property
        def deposito(self):
            return self._deposito

        @deposito.setter
        def deposito(self, value):
            self._deposito = value     

        @property
        def saque(self):
            return self._saque

        @saque.setter
        def saque(self, value):
            self._saque = value

        def operar(self):
            return self._saque + self._deposito    
  

        

#cliente = Cliente('Maria', '7499558898', 2500, 'feminino')
#print('Nome: {} \n Telefone: {} \n Renda Mensal: {} \n Genero: {}'.format(cliente.nome, cliente.telefone, cliente.renda_mensal, cliente.genero))

#conta = ContaCorrente('Maria', '7499558898', 2500, 'feminino', 'Maria', 100, 100, 100)

teste = ContaCorrente()
d = teste.deposito = 10
s = teste.saque = 10
op = teste.operar()



     
            


        
