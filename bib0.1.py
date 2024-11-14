"""
Programa: BIB01
Titulo  : Sistema Gestão de Biblioteca
Tipo    : Programa
Finalid : Gerenciamento Avançado de Livros
Autores : Kaique Chaves, Rodolfo Sousa, Camila Costney, Winicius Passaia, Maria Eduarda
Data    : 13-11-2024
Solicit : Pedriana Pavão 
Demanda : Avaliação Qualitativa Algoritmos e Linguagens de Programação

"""
## Importando Biblioteca
## definindo a biblioteca com nomenclatura abreviada
import datetime as data
import time as tempo

## Criando Dicionarios de Dados com Listas por Cadastro
dicionarioBiblioteca = {
    "autores": [] ,
    "livros": [] ,
    "alunos": [] ,
    "emprestimos": []
}


## DEFININDO FUNÇÃO PARA ENFEITE
def mostraLinha():
    print("-" * 60)


##Definindo Função para Cadastro de Livro na lista 
def cadastraLivro(id,titulo,autor,dataCadastro = None,dataAtualizacao = None,disponivel = True):
    if dataCadastro is None:
        data.datetime.now().strftime("%d/%m/%y") ##FUNÇÃO PARA COLOCAR AUTOMATICO A DATA DO CADASTRO E DEFINIR A DATA COMO STRING
    
    elif dataAtualizacao is None:
        data.datetime.now().strftime("%d/%m/%y") ##FUNÇÃO PARA COLOCAR AUTOMATICO A DATA DA ALTERAÇÃO E DEFINIR A DATA COMO STRING
 ##abrindo dicionario para adicionar dentro da lista
    addlivro = {
        "id": id,
        "titulo": titulo,
        "autor": autor,
        "dataCadastro": dataCadastro,
        "dataAtualizacao": dataAtualizacao,
        "disponivel": True
    }
    ##adicionando na lista o dicionario com append
    dicionarioBiblioteca["livros"].append(addlivro)


##Definindo Função que Cadastra o Autor
def cadastraAutor(id,nome,dataNascimento):
    #abrindo dicionario para adicionar a lista
    addAutor = {
        "id": id,
        "nome": nome,
        "dataNascimento": dataNascimento
    }
    ##aducuinando na lista o dicionariio com o append
    dicionarioBiblioteca["autores"].append(addAutor)


##Definindo Função que cadastra o aluno
def cadastraAluno(id,nome,dataNascimento):
    #abrindo dicionario para adicionar a lista
    addAluno = {
        "id": id,
        "nome": nome,
        "dataNascimento": dataNascimento
    }
    #adicionando na lista o dicionario com o append
    dicionarioBiblioteca["alunos"].append(addAluno)


##Definindo função de busca livro por titulo
def buscaLivrotit(titulo):
    return [livro for livro in dicionarioBiblioteca["livros"]
            if titulo.lower() in livro["titulo"]  ## função com llower para deixar tudo em letra minuscula
            ] 
    

##Definindo Função de disponibilidade de livros
def livrosDisp():
    for livro in dicionarioBiblioteca["livros"]:
        print(f"dados do livro {livro["disponivel"]} ")
        if livro["disponivel"] == True:
         print(f"o Documento em Questão {livro["id"]} {livro["titulo"]} disponivel desde {livro["dataAtualizacao"]} ")

##Definindo função de emprestimo de livros
def emprestimoLivro(livroId,alunoId):
    for livro in dicionarioBiblioteca["livros"]:
     if livro["id"] == livroId and livro["disponivel"]==True:
         #verificar se o aluno existe
        if dicionarioBiblioteca["alunos"] == alunoId:
           print(dicionarioBiblioteca["alunos"])
        else:
            print(f""" HELP!! ALUNO NÃO CADASTRADO""")
            cadastraAluno()

        #senao aluno não cadastrado
     else:
         print("")
         #livro indisponivel

##Definindo função de busca livro por id
def buscaLivroid(id):
    return [livro for livro in dicionarioBiblioteca["livros"]]

            
##Definindo Função de busca aluno
def buscaAlunos(nome):
    return [aluno for aluno in dicionarioBiblioteca["alunos"]]


## INICIO DO MENU DEFININDO A FUNÇÃO 
def menuInicial():
    while True:
        mostraLinha()
        print(f""" \n
                  [1] - Relatorio de Livros Disponiveis
                  [2] - Relatorio de Autores 
                  [3] - Relatorio Alunos Cadastrados 
                  [4] - Cadastrar Livro
                  [5] - Cadastrar Autor
                  [6] - Cadastrar Aluno
                  [7] - Emprestimo de Livro
                  [0] - Sair
               """)
        
        ##INPUT PARA GUARDAR A OPÇÃO SELECIONADA PELO USUARIO
        mostraLinha()
        escolha = int(input("Digite a numeração de uma das opções acima: "))
        mostraLinha()

## chamando as funções para suas respectivas opções do menus
        if escolha == 1:
            mostraLinha()
            print(f"Os livros disponiveis são {livrosDisp()} ")
            mostraLinha()
        
        elif escolha == 2:
            mostraLinha()
            print(dicionarioBiblioteca["autores"])
            mostraLinha()

        elif escolha == 3:
            mostraLinha()
            print(dicionarioBiblioteca["alunos"])
            mostraLinha()
        
        elif escolha == 4:
            mostraLinha()
            print("para cadastrar um livro segue dados necessarios")
            mostraLinha()
            id = int(input("ID do livro :"))
            titulo = str(input("Titulo do Livro: "))
            autor = str(input("Autor: "))
            dataCadastro = data.datetime.now().strftime("%d/%m/%y")
            dataAtualizacao = data.datetime.now().strftime("%d/%m/%y")
            disponivel = True
            cadastraLivro(id,titulo,autor,dataCadastro,dataAtualizacao,disponivel)
            print("Cadastrado com Sucesso")
            mostraLinha()
        
        elif escolha == 5:
            mostraLinha()
            print(f"Para cadastrar um autor por favor preencher os campos abaixo")
            id = int(input("ID :"))
            nome = str(input("NOME : "))
            dataNascimento = str(input("DATA DE NASCIMENTO : "))
            cadastraAutor(id,nome,dataNascimento)
            print("Cadastrado com Sucesso")
            mostraLinha()

        elif escolha == 6:
            mostraLinha()
            print(f"Para cadastrar o aluno preencher os campos abaixo")
            id = int(input("ID do Aluno: "))
            nome = str(input("Nome do Aluno: "))
            dataNascimento = str(input("Data de Nascimento: "))
            cadastraAluno(id,nome,dataNascimento)
            print("Cadastrado com Sucesso")

        elif escolha == 7:
            mostraLinha()
            print(f"LIVROS DISPONIVEIS {livrosDisp()}")
            livrosDisp(titulo)
            livroId = int(input("Digite o ID do livro: "))
            alunoId = int(input("Digite o ID do aluno: "))
            emprestimoLivro(livroId, alunoId)
            print("")


        elif escolha == 0:
            print("Sistema está se encerrando...⏳")
            for i in range(5, -1, -1):
                print(i, end= "\r")

                tempo.time.sleep(0.6)
            print("Sistema se encerrou!✅")
            break

        else:
            print("opção invalida")

menuInicial()