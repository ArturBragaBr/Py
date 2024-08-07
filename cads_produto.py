from classe_Produto import Produto


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