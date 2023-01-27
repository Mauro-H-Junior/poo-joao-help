from Models import *

class DAOCategoria:
    @classmethod
    def salvar(cls, categoria):
        print('salvar')
        with open('categoria.txt', 'a') as arquivo:
            arquivo.write(categoria + '\n')

    @classmethod
    def ler(cls):
        print('ler')

        with open('categoria.txt', 'r') as  arquivo:
            categoria = arquivo.readlines()

            lista_strip = []
            for i in categoria:
                j = i.strip('\n')
                lista_strip.append(j)

        # ou de forma funcional
        # categoria = list(map(lambda x: x.replace('\n', ''), categoria))

        cat = []
        for i in lista_strip:
            cat.append(Categoria(i))

        return cat

# DAOCategoria.salvar('MERCEARIA')
# DAOCategoria.salvar('FRIOS')
# DAOCategoria.salvar('CONGELADOS')

# x = DAOCategoria.ler()
# # print(x[2].categoria)

class DAOVenda:

    @classmethod
    def salvar(cls, venda: Venda):
        with open('venda.txt', 'a') as arquivo:
            arquivo.write(venda.itensvendidos.nome + "|" +  venda.itensvendidos.preco + "|" + venda.itensvendidos.categoria + "|" + 
            venda.vendedor + "|" + venda.cliente + "|" + str(venda.qtdevendida) + "|" + str(venda.data) + '\n') 
    
    @classmethod
    def ler(cls):
        with open('venda.txt', 'r') as arquivo:
            venda = arquivo.readlines()
            
            lista_strip = []
            for i in venda:
                j = i.strip('\n')
                l = j.split('|')
                lista_strip.append(l)

        # print(lista_strip)

        # ou de forma funcional
        # categoria = list(map(lambda x: x.replace('\n', ''), categoria))
        # categoria = list(map(lambda x: x.split('|'), categoria))

        vend = []
        for i in lista_strip:
            vend.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
        return vend


# x = Produtos('macarrao','R$11,00', 'MERCEARIA')
# y = Venda(x, 'nomevendedor', 'nomeComprador', '3')

# DAOVenda.salvar(y)
# x = DAOVenda.ler()
# print(x[0].vendedor)

class DAOProduto:

    @classmethod
    def salvar(cls, produto: Produtos):
        with open ('produto.txt', 'a', encoding='UTF-8') as arquivo:
            arquivo.write(produto.nome + "|" + produto.preco + "|" + produto.categoria + '\n')

x = Produtos('MACARRÃO','R$11,00', 'MERCEARIA')
DAOProduto.salvar(x)

