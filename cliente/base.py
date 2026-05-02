from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    @abstractmethod
    def add_conta(self, conta):
        pass

    @abstractmethod
    def remover_conta(self, conta):
        pass

    def __str__(self):
        return f"Cliente: {self.nome}, Contas: {len(self.contas)}"



class ClienteFisico(Cliente):
    def __init__(self, nome, cpf):
        super().__init__(nome)
        self.cpf = cpf
    
    def add_conta(self, conta):
        self.contas.append(conta)
    
    def remover_conta(self, conta):
        self.contas.remove(conta)
    
    @property
    def documento(self):
        return self.cpf
    
    def __str__(self):
        return f"Cliente: {self.nome}, Documento: {self.cpf}, Contas: {len(self.contas)}"

class ClienteJuridico(Cliente):
    def __init__(self, nome, cnpj):
        super().__init__(nome)
        self.cnpj = cnpj
    
    def add_conta(self, conta):
        self.contas.append(conta)
    
    def remover_conta(self, conta):
        self.contas.remove(conta)
    
    @property
    def documento(self):
        return self.cnpj
    
    def __str__(self):
        return f"Cliente: {self.nome}, Documento: {self.cnpj}, Contas: {len(self.contas)}"
