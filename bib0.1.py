print("""
Programa: BIB01
Titulo  : Sistema Gestão de Biblioteca
Tipo    : Programa
Finalid : Gerenciamento Avançado de Livros
Autores : Kaique Chaves, Rodolfo Sousa, Camila Costney, Winicius Passaia, Maria Eduarda
Data    : 13-11-2024
Solicit : Pedriana Pavão 
Demanda : Avaliação Qualitativa Algoritmos e Linguagens de Programação

""")

## Importando Biblioteca
import datetime as data
import time as tempo

#sistema simples de carregamento, apenas enfeite para ficar bonito
print(" ---------|📚 Biblioteca Cest 📚|---------\n")
for i in range(11): 
    print(f"Carregando: {'🟨' * i}{'◽' * (10 - i)} {i * 10}% ", end="\r")
    tempo.sleep(0.8)
print(end="Carregado com Sucesso\n")



## Criando Dicionarios de Dados com Listas por Cadastro
dicionarioBiblioteca = {
    "autores": [],
    "livros": [],
    "alunos": [],
    "emprestimos": []
}

## DEFININDO FUNÇÃO PARA ENFEITE
def mostraLinha():
    print("-" * 60)

## Definindo Função para Cadastro de Livro na lista 
def cadastraLivro(id, titulo, autor, dataCadastro=None, dataAtualizacao=None, disponivel=True):
    if dataCadastro is None:
        dataCadastro = data.datetime.now().strftime("%d/%m/%y")
    if dataAtualizacao is None:
        dataAtualizacao = data.datetime.now().strftime("%d/%m/%y")
    
    addlivro = {
        "id": id,
        "titulo": titulo,
        "autor": autor,
        "dataCadastro": dataCadastro,
        "dataAtualizacao": dataAtualizacao,
        "disponivel": disponivel
    }
    dicionarioBiblioteca["livros"].append(addlivro)

## Definindo Função que Cadastra o Autor
def cadastraAutor(id, nome, dataNascimento):
    addAutor = {
        "id": id,
        "nome": nome,
        "dataNascimento": dataNascimento
    }
    dicionarioBiblioteca["autores"].append(addAutor)

## Definindo Função que cadastra o aluno
def cadastraAluno(id, nome, dataNascimento):
    addAluno = {
        "id": id,
        "nome": nome,
        "dataNascimento": dataNascimento
    }
    dicionarioBiblioteca["alunos"].append(addAluno)

## Definindo função de busca livro por titulo
def buscaLivrotit(titulo):
    return [livro for livro in dicionarioBiblioteca["livros"]
            if titulo.lower() in livro["titulo"].lower()]

## Definindo Função de disponibilidade de livros
def livrosDisp():
    for livro in dicionarioBiblioteca["livros"]:
        if livro["disponivel"]:
            print(f"O livro {livro['id']} {livro['titulo']} disponível desde {livro['dataAtualizacao']}")

## Definindo função de emprestimo de livros
def emprestimoLivro(livroId, alunoId):
    livro_encontrado = next((livro for livro in dicionarioBiblioteca["livros"] if livro["id"] == livroId and livro["disponivel"]), None)
    if livro_encontrado:
        aluno_encontrado = next((aluno for aluno in dicionarioBiblioteca["alunos"] if aluno["id"] == alunoId), None)
        if aluno_encontrado:
            livro_encontrado["disponivel"] = False
            print(f"Livro {livro_encontrado['titulo']} emprestado ao aluno {aluno_encontrado['nome']}.")
        else:
            print("⚠️AVISO! ALUNO NÃO CADASTRADO")
            id = int(input("Digite o ID do aluno: "))
            nome = str(input("Nome do Aluno: "))
            dataNascimento = str(input("Data de Nascimento: "))
            cadastraAluno(id, nome, dataNascimento)
            print("Aluno cadastrado com sucesso.")
    else:
        print("Livro não disponível ou não encontrado.")

## Definindo função de busca livro por id
def buscaLivroid(id):
    return [livro for livro in dicionarioBiblioteca["livros"] if livro["id"] == id]

## Definindo Função de busca aluno
def buscaAlunos(nome):
    return [aluno for aluno in dicionarioBiblioteca["alunos"] if nome.lower() in aluno["nome"].lower()]

## INICIO DO MENU DEFININDO A FUNÇÃO 
def menuInicial():
    while True:
        mostraLinha()
        print(f""" 
                  [1] - Cadastrar Autor
                  [2] - Cadastrar Aluno
                  [3] - Cadastrar Livro
                  [4] - Autores Cadastrados 
                  [5] - Alunos Cadastrados 
                  [6] - Deseja perdir um Livro Emprestado?
                  [7] - Livros Disponíveis para Emprestimo
                  [0] - Sair
               """)
        
        mostraLinha()
        escolha = int(input("Digite a numeração de uma das opções acima: "))
        mostraLinha()

        if escolha == 1:
            mostraLinha()
            print("Para cadastrar um autor, por favor preencher os campos abaixo")
            id = int(input("ID: "))
            nome = str(input("NOME: "))
            dataNascimento = str(input("DATA DE NASCIMENTO: "))
            cadastraAutor(id, nome, dataNascimento)
            print("Cadastrado com Sucesso")
            mostraLinha()

        elif escolha == 2:
            mostraLinha()
            print("Para cadastrar o aluno, preencher os campos abaixo")
            id = int(input("ID do Aluno: "))
            nome = str(input("Nome do Aluno: "))
            dataNascimento = str(input("Data de Nascimento: "))
            cadastraAluno(id, nome, dataNascimento)
            print("Cadastrado com Sucesso")
            mostraLinha()

        elif escolha == 3:
            mostraLinha()
            print("Para cadastrar um livro, siga os dados necessários")
            mostraLinha()
            id = int(input("ID do livro: "))
            titulo = str(input("Título do Livro: "))
            autor = str(input("Autor: "))
            cadastraLivro(id, titulo, autor)
            print("Cadastrado com Sucesso")
            mostraLinha()

        elif escolha == 4:
            mostraLinha()
            print(dicionarioBiblioteca["autores"])
            mostraLinha()

        elif escolha == 5:
            mostraLinha()
            print(dicionarioBiblioteca["alunos"])
            mostraLinha()

        elif escolha == 6:
            mostraLinha()
            livrosDisp()
            livroId = int(input("Digite o ID do livro: "))
            alunoId = int(input("Digite o ID do aluno: "))
            emprestimoLivro(livroId, alunoId)
            mostraLinha()

        elif escolha == 7:
            mostraLinha()
            print(dicionarioBiblioteca["livros"])
            mostraLinha()

        elif escolha == 0:
            print("Sistema está se encerrando...⏳")
            for i in range(5, -1, -1):
                print(i, end="\r")
                tempo.sleep(1)
            print("Sistema se encerrou!✅")
            break

        # SIMPLES, SE NAO FOR UMA DAS OPÇÕES DO MENU, APARECE O PRINT AVISANDO
        elif escolha not in [0, 1, 2, 3, 4, 5, 6, 7]:
            print("Opção inválida. Tente novamente.")
        

menuInicial()