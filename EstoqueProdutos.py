#criando o dicionário
produto ={}

#criação de funções

def adicionar():
    nome = input("Digite o nome do produto: ").strip().lower()
    if not nome:
        print("Erro: O nome do produto não pode ficar em branco.")
        return
    try:
        quantidade = int(input("Digite a quantidade do produto: "))
        produto[nome]= quantidade
        print(f"O produto {nome} foi adicionado com sucesso!")
    except ValueError:
        print("Você não digitou o número correspondente a quantidade")

def listar():
    nome = input("Digite o nome do produto que deseja buscar: ").strip().lower()
    if nome in produto:
        quantidade = produto[nome]
        print(f"Produto: {nome} | Quantidade: {quantidade}")
    else:
        print("Produto não se encontra no estoque")

def atualizar():
    try:
        nome = input("Digite o nome do produto que deseja atualizar: ").strip().lower()
        if nome in produto:
            quantidadeAtual = int(input("Digite a quantidade que deseja atualizar: "))
            produto[nome]= quantidadeAtual
            print(f"Produto {nome} atualizado com sucesso")
        else:
            print("Produto não se encontra no estoque")
    except ValueError:
        print("Você não digitou um número correspondete a quantidade")


#Main

while True:
    print("===== Gerenciador de Produtos =====")
    print("1. Adicionar produto")
    print("2. Listar produto")
    print("3. Atualizar produto")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        atualizar()
    elif opcao == "4":
        print("Encerrando o programa. Até logo!")
        break
    else:
        print("Erro: Opção inválida. Tente novamente.")