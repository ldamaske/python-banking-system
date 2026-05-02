class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.agencias = []
        self.clientes = []
        self.contas = []

    def add_agencia(self, agencia):
        self.agencias.append(agencia)

    def add_cliente(self, cliente):
        self.clientes.append(cliente)

    def add_conta(self, conta):
        self.contas.append(conta)

    def __str__(self):
        return f"Banco: {self.nome}, Agências: {len(self.agencias)}, Clientes: {len(self.clientes)}, Contas: {len(self.contas)}"