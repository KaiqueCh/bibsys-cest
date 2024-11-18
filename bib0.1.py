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
##importando funções
from funcbib01 import dicionarioBiblioteca, cadastraAluno, cadastraAutor, cadastraLivro, emprestimoLivro, mostraLinha, livrosDisp, buscaAlunos, buscaLivroid, buscaLivrotit,menuInicial

## Importando Biblioteca Necessarias para execução das Funções
import datetime as data
import time as tempo

#sistema simples de carregamento, apenas enfeite para ficar bonito
print(" ---------|📚 Biblioteca Cest 📚|---------\n")
for i in range(11): 
    print(f"Carregando: {'🟨' * i}{'◽' * (10 - i)} {i * 10}% ", end="\r")
    tempo.sleep(0.8)
print(end="Carregado com Sucesso\n")

menuInicial()