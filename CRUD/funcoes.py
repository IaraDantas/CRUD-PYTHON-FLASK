####################################################################################
# TITULO do arquivo python: funcoes.py
# AUTOR: Iara de Melo Dantas Bezerra
# Data: 25/11/222 | PERIODO: 2022.2  | PROJETO: Completo | Versão: 0.2
# OBJETIVO DESSE ARQUIVO: Criar as funções usadas pelo servidor.py [CRUD].
####################################################################################
# importar bibliotecas e modulos necessários
import sqlite3

# CRUD - CRIAR | CONSULTAR | ATUALIZAR | DELETAR
conexao_bd = None

def iniciar():
    global conexao_bd
    conexao_bd = sqlite3.connect("banco\database.db")


def listar_tabela(tabela): # função usada para listar a tabela escolhida
    iniciar()
    conex_c = conexao_bd.cursor()
    conex_sel = conex_c.execute("SELECT * FROM %s" % tabela)
    conexao_bd.commit()
    resp = conex_sel.fetchall()
    conex_c.close()
    return resp

def validar_campo(campo_teste, tabela, campo_tabela):
    iniciar()
    conex_c = conexao_bd.cursor()
    conex_sel = conex_c.execute("SELECT * FROM %s WHERE %s = '%s'" % (tabela, campo_tabela, campo_teste))
    conexao_bd.commit()
    resp = conex_sel.fetchall()
    conex_c.close()
    return resp


def teste_try(variavel):
    cont = 0
    try:
        variavel = int(variavel)
        cont += 0
    except:
        cont += 10
    return cont

def validar_nome(nome_teste):
    contador = 0
    nome = nome_teste.split(' ')
    lista = []
    for i in nome:
        if i != ' ' and i != '':
            lista.append(i)
    textual = teste_try(nome_teste)
    if len(lista) > 1 and textual > 0:
        contador += 10
    else:
        contador += 0
    return contador

def email_certo (email):
    contador = 0
    lista = email.split("@")
    l = lista[0]
    if teste_try(email) > 0 and len(lista) == 2 and len(lista[0]) >= 1 and len(lista[1]) > 5 and len(
            email.split(" ")) == 1:
        if len(l.split(".com")) == 1 or len(l.split(".com.br")) == 1:
            l2 = lista[1]
            if len(l2.split(".com")) == 2 or len(l2.split(".com.br")) == 2:
                contador += 10
            else:
                pass
        else:
            pass
    else:
        pass
    return contador

def endereco_certo(endereco):
    existe = (validar_campo(endereco, 'hospital', 'endereco'))
    cont = 0
    if len(existe) == 1:
        if endereco == existe[0][2]:
            cont += 10
        else:
            cont-=10
        cont += 5
    return cont

