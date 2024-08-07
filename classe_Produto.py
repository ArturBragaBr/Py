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