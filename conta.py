from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    def __init__(self, conta, agencia, saldo):
        self.conta = conta
        self.agencia = agencia
        self._saldo = saldo

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass
    
    @property
    def saldo(self):
        return self._saldo

class ContaCorrente(ContaBancaria):
    def __init__(self, conta, agencia, saldo, limite=1000):
        super().__init__(conta, agencia, saldo)
        self.limite = limite
    
    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self._saldo -= valor
        else:
            raise ValueError("Saldo insuficiente")

    def depositar(self, valor):
        self._saldo += valor
    
    def __str__(self):
        return f"Conta Corrente: {self.conta}, Agência: {self.agencia}, Saldo: R$ {self.saldo}, Limite: R$ {self.limite}"

class ContaPoupanca(ContaBancaria):
    def __init__(self, conta, agencia, saldo):
        super().__init__(conta, agencia, saldo)
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self._saldo -= valor
        else:
            raise ValueError("Saldo insuficiente")

    def depositar(self, valor):
        self._saldo += valor
    
    def __str__(self):
        return f"Conta Poupança: {self.conta}, Agência: {self.agencia}, Saldo: R$ {self.saldo}"