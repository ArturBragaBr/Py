class Produto:
    def __init__(self, codproduto, nome, descricao, tamanho, preco):
        self.codproduto = codproduto
        self.nome = nome
        self.descricao = descricao
        self.tamanho = tamanho
        self.preco = preco

    def calcular(self):
        desconto = self.preco * 0.10
        preco_desconto = self.preco - desconto
        print(f"O preço com desconto do Produto {self.preco} é R$ {preco_desconto:.2f}")

produtos = []

while True:
    resp = input('ENTER PARA CADASTRAR DADOS OU DIGITE S PARA SAIR: ')

    if resp == 'S' or resp == 's':
        break

    codproduto = input('Digite o código do Produto: ')
    nome = input('Digite o nome do Produto:')
    descricao = input('Digite a descrição do Produto:')
    tamanho = input('Digite o tamanho: ')
    preco = input('Digite o preço do Produto: ')

    produto = Produto(codproduto, nome, descricao, tamanho, preco)

    produtos.append(produto)

print('Lista de Produtos')
print('nome \tDescrição\tPreço'.expandtabs(20))
for prod in produtos:
    print(f"{prod.nome}\t{prod.descricao}\t{prod.preco}".expandtabs(20))






