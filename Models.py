from datetime import datetime

class Categoria:
    def __init__(self, categoria): # na categoria eu posso deixar só a string sozinha se informar o "tipo" pois só tenho a categoria msm
        self.categoria = categoria

class Produtos:
    def __init__(self, nome, preco, categoria) -> None: 
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Estoque:
    def __init__(self, produto: Produtos, qtde) -> None:
        self.produto = produto
        self.qtde = qtde

class Venda:
    def __init__(self, itensvendidos: Produtos, vendedor, cliente, qtdevendida, data = datetime.now().strftime("%d/%m/%Y")) -> None:
        self.itensvendidos = itensvendidos
        self.vendedor = vendedor
        self.cliente = cliente
        self.qtdevendida = qtdevendida
        self.data = data

class Forcecedor:
    def __init__(self, nome, cnpj, telefone, categoria) -> None:
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria

class Pessoa:
    def __init__(self, nome, telefone, cpf, email, endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email
        self.endereco = endereco

class Funcionario(Pessoa):
    def __init__(self, clt, nome, telefone, cpf, email, endereco):
        self.clt = clt
        super().__init__(nome, telefone, cpf, email, endereco)



