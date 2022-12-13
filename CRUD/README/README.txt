####################################################################################
# TITULO do arquivo python: servidor.py
# AUTOR:
# Data: 25/11/222 | PERIODO: 2022.2  | PROJETO: EM CURSO | Versão: 0.2
# OBJETIVO DESSE ARQUIVO: Explicar o funcionamento do programa e sua execução.
#
# CONTEÚDO:
#   SOBRE O FUNDAMENTO TEÓRICO DO CÓDIGO E SUA FUNCIONALIDADE
#	1 BREVE DESCRIÇÃO DO PROGRAMA E SEU RESULTADO
#	2 PREREQUISITOS E AMBIENTE DE EXECUÇÃO - Como executar este programa
#	3 SOBRE O CÓDIGO
#       3.1 BANCO DE DADOS - SCRIPT
#       3.2 FUNÇÕES
#       3.3 SERVIDOR - FLASK
#	4 SOBRE O RESULTADO - Explicação da obtenção dos resultados
#
####################################################################################

SOBRE O FUNDAMENTO TEÓRICO DO CÓDIGO E SUA FUNCIONALIDADE

         Os bancos de dados permitem que informações sejam ordenadas e armazenadas,
    para realizar a manipulação destes, há a estrutura CRUD (Criar, Consultar, Atualizar
    e Deletar), destaca-se que, esta estrutura pode ser acessada via navegador, para
    tal, a linguagem de programação será um agemte intermediário entre o usuário via web e
    o banco de dados (myslq, mysqlite, mongodb, ....). Em Python, para a elaboração do CRUD
    com acesso via navegador, há uma série de ferramentas e frameworks que possibilitam isto.
    Das quais, destaca-se o microframework Flask, usado neste projeto, em relação ao banco
    de dados, foi-se adotado o banco MySQLite, apenas pela natureza otimizada de reduzir
    processamento no projeto, motivo que é amplamente usado em aplicações móveis. Dessa
    forma, evidencia-se a aplicabilidade do python para propor soluções viáveis às novas
    necessidades e demandas. Das quais, cita-se a questão do monitoramento e gestão da saúde
    frente aos casos de Covid-19 (pandemia no Novo Coronavírus, notificada desde 2019, seguindo
    até a data deste projeto), que gera comprometimento respiratório e pode levar ao óbito,
    motivo que justifica os esforços em prol de reduzir os casos de Covid-19.


####################################################################################
        1  BREVE DESCRIÇÃO DO PROGRAMA E SEU RESULTADO


        No contexto apresentado, este projeto apresenta um banco de dados que possui tabelas
    referentes aos hospitais (onde profissionais trabalham e pacientes ficam internados),
    aos profissionais de saude, que trabalham em hospitais com pacientes variados, e uma
    referente aos pacientes internados em hospitais, que podem estar ou não com Covid-19.
    Assim como, apresenta um código escrito em Python que, conecta o banco de dados com
    o usuário via navegador (web service), e forma que permite INSERIR (cadastrar pacientes,
    profissionais e hospitais da rede estadual de saúde), CONSULTAR (consultar os dados
    presentes em cada tabela), ATUALIZAR (atualizar dados já cadastrados nas tabelas) e
    DELETAR (excluir dados da tabela), no caso, uma CRUD.



####################################################################################
        2  PREREQUISITOS E AMBIENTE DE EXECUÇÃO - Como executar este programa


Após realizar o download e instalação do interpretador Python3, deve-se instalar o IDE Pycharm,
indicando, o Python3 como interpretador, defina o nome do diretório principal do projeto da forma
que interessar, por exemplo: 'CRUD_Python', e ao criar seu diretório principal é necessário a
importação das bibliotecas utilizadas pelo programa, pois, o Python possui várias bibliotecas NATIVAS
que são instaladas junto com o interpretador, mas, algumas necessitam serem agregadas ao programa
separadamente, como ocorreu com as bibliotecas FLASK, REQUESTS [...] que o procedimento
para sua instalação será descrito neste arquivo.
     Além da importação da bibliotecas, deve-se manter o arquivo de banco de dados NO MESMO DIRETÓRIO
que o pograma, PARA QUE NÃO NECESSITE DE AJUSTES, pois, está configurado para buscar o arquivo
"database.db" no mesmo diretório, caso NÃO ESTEJA NO MESMO DIRETÓRIO, deverá inserir manualmente o
CAMINHO DO ARQUIVO na variável indicada no programa.

                2.1 PARA ENCONTRAR E INSTALAR AS BIBLIOTECAS

  	Para a elaboração deste trabalho, foi necessário o uso das bibliotecas a seguir.
  para sua agregação ao código, deve-se:

  1º: No MENU SUPERIOR do Pycharm, selecionar a OPÇÃO 'FILE';
  2º: Escolher a OPÇÃO 'SETTINGS' (ou executar o comando 'Ctrl + Alt + S');
  3º: Em Settings, no menu lateral a ESQUERDA, selecionar a OPÇÃO PROJETCT:'NomedoProjeto' (6ª opção de cima para baixo);
  4º: Dentro do projeto, deve-se selecionar a OPÇÃO 'Python Interpreter' (Interpretador Python);
  5º: No centro da tela, será listado os pacotes já contidos no interpretador e sua versão mais atual instalada;
  6º: Selecionar a OPÇÃO de adicionar pacotes, representada pelo simbolo de adicção '+', na lateral DIREITA da tela;
  7º: Será aberto uma nova guia, contendo os pacotes disponíveis ('Available Packeges');
  8º: No local superior desta guia, indicado pelo simbolo de uma lupa (pesquisa), deve-se digitar o NOME DA BIBLIOTECA;
  9º: Buscar a biblioteca 'FLASK';
  10º: Será listado TODAS AS BIBLIOTECAS com relação ao pesquisado, mas, selecione APENAS a biblioteca com o nome indicado neste arquivo;
  11º: Após selecionar a biblioteca, aparecerá ao lado DIREITO da tela, as informações do pacote (autor, versão e site, ...);
  12º: Após conferir, deve-se, pressionar na OPÇÃO DE INSTALAÇÃO DO PACOTE no canto inferior da tela ('Install Package');
  13º: Após a mensagem de instalação comcluida com sucesso, busque as demais bibliotecadas (uma por vez);
  [...]
  º: Após a instalação destas, feche esta guia (voltando ao 'Settings') e confirme os novos pacotes instalados, em seguida feche esta guia.


     Em seguida, após as bibliotecas instaladas e os arquivos em mesmo diretório, pode-se executar o código, destaca-se
     que, frente a necessidade e dependencia do código estar associado ao banco de dados este necessida estar devidamente
     configurado. Para configurar o banco de dados no pycharm:

     1º: Verifique que o projeto está dividido da seguinte forma:
            Diretório 'CRUD'
                Diretorio 'banco'
                    Arquivo 'database.db'
                    Arquivo 'script.sql'
                Diretorio 'README'
                    Arquivo 'README.txt'
                Diretorio 'templates'
                    Arquivo 'index.html'
                    Arquivo 'atualizar.html'
                    Arquivo 'cadastro.html'
                    Arquivo 'consulta.html'
                    Arquivo 'index.html'
		    Arquivo 'error.html'
                    Arquivo 'remocao.html'
                Arquivo 'funcoes.py'
                Arquivo 'servidor.py'

     2º: No MENU SUPERIOR do Pycharm, selecionar a OPÇÃO 'FILE';
     3º: Escolher a OPÇÃO 'SETTINGS' (ou executar o comando 'Ctrl + Alt + S');
     3º: Selecionar a opção 'PLUGINS' (quarta opção);
     4º: Clicar sobre a lupa de busca e digitar 'Database Navigator';
     5º: Instalar o plugin 'Database Navigator' e fechar essa janela;
     6º: Clicar sobre o nome do plugin no menu superior e escolher a opção: 'Database Brwser';;
     7º: Abrirá uma divisão lateral da guia, contendo opções do banco de dados;
     8º: Clique no simbolo de adição ("+");
     9º: Aparecerá uma lista com os bancos de dados compativeis;
     10º: Selecione o banco de dados 'MySQLite';
     11º: Será aberto uma nova janela de configurações referente ao banco de dados;
     12: Na guia 'Database', insira uma descrição e um nome para a conexão;
     13º: Em seguida, pressione no nome 'sqlite.db', e clique nos 3 pontos ao final da linha;
     14º: Aparecerá a arvore de diretórios, percorra a arvore e selecione o arquivo presente neste projeto ("database.db")
     15º: Clique na guia 'Properties' e selecione a opção de 'Auto-commit';
     16º: Após, volte na guia 'Database' e pressione na opção 'Test-connection';
     17º: Confirme que o teste da coneção apresentou com sucesso, clique em 'APPLY' e feche essa janela;
     18º: Após, clique duas vezes sobre o arquivo 'script.sql' para abri-lo na guia de edição;
     19º: Ao abrir esse arquivo, na parte superior, será apresentado a opção de conectar um banco de dados;
     20º: selecione a coneção definida no passo 12º dessa orientação;
     21º: Clique no simbolo de uma "Folha com um triangulo verde", referente ao comando de 'Execute SQL Script';
     22º: Se certifique que não ocorreu erros, com essa etapa, as tabelas devem ser criadas e estarem sem informações;
     23º: Agora, no diretório principal 'CRUD', pressione no arquivo 'servidor.py' duas vezes e execute-o;
     24º: Acesse o link informado e siga as opções e orientações.

     o Pycharm disponibiliza o COMANDO 'Crtl + Shift + F10' (com o cursor pressionado no programa); pode-se
ainda, ao pressionar o botão DIREITO do mouse (dentro do código), selecionar a OPÇÃO "RUN", que executará o código de
imediato, plotando os gráficos referentes ao estudo, isto, no arquivo nomeado 'servidor.py'.



####################################################################################
        3  SOBRE O CÓDIGO

    Este projeto está dividido em arquivos, nomeados como 'servidor.py', 'funcoes.py',
'readme.txt', 'script.sql', 'database.db' e os arquivos .html. O arquivo 'funcoes.py'
será responsável por importar as bibliotecas necessárias conter funções do código,
já o arquivo 'servidor.py', será o arquivo principal, ou seja, será resposável por
importar o módulo functions e desenvolver as funcionalidades do projeto, o arquivo
'script.sql' será responsável pela criação das tabelas no banco de dados, sendo representado
pelo arquivo 'database.db'. Tem-se ainda o arquivo 'readme.txt', que apresentará as informações
acerca do projeto e seus prerequisitos, além de explicar acerca de sua funcionalidade, resultado
e execução, em relação aos arquivos .html, são os arquivos que permitem a interação com o usuário
via navegador.

        3.1 BANCO DE DADOS - SCRIPT

    O arquivo 'script.sql' é um script que contém os códigos para a criação das tabelas:
    hospital, profissional e pacientes, sendo relacionadas entre si (profissional >
    trabalha em um ou mais > hospital | profissional > é responsável por um ou mais >
    paciente | paciente > está internado em um > hospital | paciente > é responsabilidade
    de um > profissional)

create table hospital(
    id_hospital integer primary key autoincrement,
    nome text not null unique,
    endereco text not null unique,
    especialidade text not null
);

-- Cria a tabela profissional
CREATE TABLE profissional(
    id_profissional integer primary key autoincrement,
    nome varchar(100) not null,
    local_trabalho integer not null,
    cargo VARCHAR(50) not null,
    salario integer not null,
    cpf INT NOT NULL unique,
    email VARCHAR(20),
    telefone INT NOT NULL,
    foreign key(local_trabalho) references hospital(id_hospital) on delete restrict on update cascade
);

-- Cria a tabela pacientes
CREATE TABLE pacientes(
    id_paciente integer primary key autoincrement,
    nome varchar(100) not null,
    local_internado integer not null,
    profissional_responsavel integer not null,
    doenca VARCHAR(50) not null,
    cpf INT NOT NULL unique,
    email VARCHAR(20),
    telefone INT NOT NULL,
    foreign key(local_internado) references hospital(id_hospital) on delete restrict on update cascade,
    foreign key(profissional_responsavel) references profissional(id_profissional) on delete restrict on update cascade
);


Destaca-se que as chaves estrangeiras referen-se aos campos das outras tabelas, indicadas no código.

        3.2 FUNÇÕES.py

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


        3.3 SERVIDOR - FLASK



# importar bibliotecas e modulos necessários
from flask import Flask, render_template, request, flash
import funcoes as fun
import sqlite3 as sql

app = Flask(__name__)

@app.route("/") # raiz - página inicial # 100% ok
@app.route("/index") # 100% ok
def index():
     return render_template("index.html") # chama o html da página inicial

@app.route("/cadastrar", methods=["POST"]) # 100% ok
def cadastrar():
    mensagem = "Cadastrar"
    return render_template("cadastro.html", msg = mensagem)

@app.route("/cadastrar-hospitais", methods=["POST", "GET"]) # 100% ok
def cadastrar_hospitais():
    if request.method == 'POST':

        nome = request.form['nome'] # texto, unico e mais de 1 caractere
        endereco = request.form['endereco'] # texto mais de 1 caractere e único
        especialidade = request.form['especialidade'] # texto mais de 1 caractere

        if len(fun.validar_campo(nome, 'hospital', 'nome')) == 0 and fun.validar_nome(nome) > 0: # se NÃO houver o msm nome
            if len(fun.validar_campo(endereco, 'hospital', 'endereco')) == 0 and fun.teste_try(endereco) > 0 and len(endereco) > 1: # se NÃO houver o endereco JÁ cadastrado
                if len(fun.validar_campo(especialidade, 'hospital', 'especialidade')) == 0 and fun.teste_try(especialidade) > 0 and len(especialidade) > 1:  # se NÃO houver o endereco JÁ cadastrado
                    con=sql.connect("banco\database.db")
                    cur=con.cursor()
                    cur.execute("insert into hospital(nome, endereco, especialidade) values (?,?,?)", (nome, endereco, especialidade))
                    con.commit() # cadastra os novos dados
                    flash("Dados cadastrados", "success")
                    mensagem = "Cadastrar hospitais"
                    return render_template("cadastro.html", msg=mensagem)
                else:  # >> mostra o erro
                    mensagem = "Especialidade vazia ou invalida, tente novamente ou consulte os dados cadastrados"
                    return render_template("error.html", msg=mensagem, dados=especialidade)
            else: #  >> mostra o erro
                mensagem = "Endereco de Hospital cadastrado ou invalido, tente novamente ou consulte os dados cadastrados"
                return render_template("error.html", msg=mensagem, dados=endereco)
        else: # >> mostra o erro
            mensagem = "Nome inválido ou Já cadastrado, tente novamente ou consulte os dados cadastrados"
            return render_template("error.html", msg=mensagem, dados=nome) # OK - 100%


@app.route("/cadastrar-profissionais", methods=["POST"]) # 100% ok
def cadastrar_profissionais():
    if request.method == 'POST':
        nome = request.form['nome_pro']
        local_trabalho = request.form['local_trabalho']
        cargo = request.form['cargo']
        salario = request.form['salario']
        cpf = request.form['cpf']
        email = request.form['email']
        telefone = request.form['telefone']


        if len(fun.validar_campo(local_trabalho, 'hospital', 'id_hospital')) > 0 and fun.teste_try(local_trabalho) < 10: # se hospital existir
            if len(fun.validar_campo(cpf, 'profissional', 'cpf')) == 0 and fun.teste_try(cpf) < 10 and len(cpf) >= 6 and len(cpf) <= 11 : # SE CPF UNICO
                if fun.teste_try(salario) < 10 and int(salario) >= 1212 and int(salario) <= 100000:
                    if fun.teste_try(telefone) < 10 and len(telefone) >= 10 and len(telefone) <= 11:
                        if fun.email_certo (email) > 0:
                            if fun.validar_nome(nome) > 0:
                                if fun.teste_try(cargo) > 0 and len(cargo) > 1:
                                    con=sql.connect("banco\database.db")
                                    cur=con.cursor()
                                    cur.execute("insert into profissional(nome, local_trabalho, cargo, salario, cpf, email, telefone) values (?,?,?,?,?,?,?)", (nome, local_trabalho, cargo, salario, cpf, email, telefone))
                                    con.commit()
                                    flash("Dados cadastrados", "success")
                                    mensagem = "Cadastrar profissionais"
                                    return render_template("cadastro.html", msg = mensagem)
                                else:  # se cargo invalido mostra o erro
                                    mensagem = "Cargo invalido, tente novamente ou consulte os dados cadastrados"
                                    return render_template("error.html", msg=mensagem, dados=cargo)
                            else:  # se nome invalido mostra o erro
                                mensagem = "Nome invalido, tente novamente ou consulte os dados cadastrados"
                                return render_template("error.html", msg=mensagem, dados=nome)
                        else:  # se email invalido mostra o erro
                            mensagem = "Email invalido, tente novamente ou consulte os dados cadastrados"
                            return render_template("error.html", msg=mensagem, dados=email)
                    else:  # se telefone invalido mostra o erro
                        mensagem = "Telefone Invalido, tente novamente ou consulte os dados cadastrados"
                        return render_template("error.html", msg=mensagem, dados=telefone)
                else:  # se salario invalido > mostra o erro
                    mensagem = "Salario Invalido!, tente novamente ou consulte os dados cadastrados"
                    return render_template("error.html", msg=mensagem, dados=salario)
            else:  # se CPF invalido > mostra o erro
                mensagem = "CPF Invalido, tente novamente ou consulte os dados cadastrados"
                return render_template("error.html", msg=mensagem, dados=cpf)
        else: # se Não houver o hospital > mostra o erro
            mensagem = "ID de Hospital Invalido, tente novamente ou consulte os dados cadastrados"
            return render_template("error.html", msg=mensagem, dados=local_trabalho) # OK - 100%


@app.route("/cadastrar-pacientes", methods=["POST"]) # 100% ok
def cadastrar_pacientes():
    if request.method == 'POST':

        nome = request.form['nome_paciente']
        local_internado = request.form['local_internado']
        profissional_responsavel = request.form['profissional']
        doenca = request.form['doenca']
        cpf = request.form['cpf_paciente']
        email = request.form['email_paciente']
        telefone = request.form['telefone_paciente']

        validar_h = fun.validar_campo(local_internado, 'hospital', 'id_hospital')

        if len(validar_h) > 0 and fun.teste_try(local_internado) < 10: # se hospital existe
            validar_cpf = fun.validar_campo(cpf, 'pacientes', 'cpf')
            if len(validar_cpf) == 0 and fun.teste_try(cpf) < 10 and len(cpf) >= 6 and len(cpf) <= 11:
                validar_profissional = fun.validar_campo(profissional_responsavel, 'profissional', 'id_profissional')
                if fun.teste_try(profissional_responsavel) < 10 and len(validar_profissional) > 0:
                    if fun.teste_try(telefone) < 10 and len(telefone) >= 10 and len(telefone) <= 11:
                        if fun.email_certo (email) > 0:
                            if fun.validar_nome(nome) > 0:
                                if fun.teste_try(doenca) > 0 and len(doenca) > 1:
                                    con = sql.connect("banco\database.db")
                                    cur = con.cursor()
                                    cur.execute(
                                        "insert into pacientes(nome, local_internado, profissional_responsavel, doenca, cpf, email, telefone) values (?,?,?,?,?,?,?)",
                                        (nome, local_internado, profissional_responsavel, doenca, cpf, email, telefone))
                                    con.commit()
                                    flash("Dados cadastrados", "success")
                                    mensagem = "Cadastrar pacientes"
                                    return render_template("cadastro.html", msg = mensagem)

                                else:  # se nome invalido mostra o erro
                                    mensagem = "Patologia invalida, tente novamente ou consulte os dados cadastrados"
                                    return render_template("error.html", msg=mensagem, dados=doenca)
                            else:  # se nome invalido mostra o erro
                                mensagem = "Nome invalido, tente novamente ou consulte os dados cadastrados"
                                return render_template("error.html", msg=mensagem, dados=nome)
                        else:  # se telefone invalido mostra o erro
                            mensagem = "Email invalido, tente novamente ou consulte os dados cadastrados"
                            return render_template("error.html", msg=mensagem, dados=email)
                    else:  # se telefone invalido mostra o erro
                        mensagem = "Telefone Invalido, tente novamente ou consulte os dados cadastrados"
                        return render_template("error.html", msg=mensagem, dados=telefone)
                else:  # se ID de profissional invalido > mostra o erro
                    mensagem = "Id de profissional invalido, tente novamente ou consulte os dados cadastrados"
                    return render_template("error.html", msg=mensagem, dados=profissional_responsavel)
            else:  # se CPF invalido > mostra o erro
                mensagem = "CPF Invalido, tente novamente ou consulte os dados cadastrados"
                return render_template("error.html", msg=mensagem, dados=cpf)
        else: # se Não houver o hospital > mostra o erro
            mensagem = "ID de Hospital Invalido, tente novamente ou consulte os dados cadastrados"
            return render_template("error.html", msg=mensagem, dados=local_internado)# OK - 100%


@app.route("/consultar", methods=["POST"]) # 100% ok
def consultar():
    mensagem = "Consultar"


    hospital = fun.listar_tabela("hospital")
    profissionais = fun.listar_tabela("profissional")
    pacientes = fun.listar_tabela("pacientes")

    return render_template("consulta.html", msg = mensagem, hospital=hospital, profissionais=profissionais, pacientes=pacientes)


@app.route("/consultar-hospitais", methods=["POST"]) # 100% ok
def consultar_hospitais():
    mensagem = "Consultar"
    hospital = fun.listar_tabela("hospital")
    return render_template("consulta.html", msg = mensagem, lista=hospital)


@app.route("/consultar-profissionais", methods=["POST"]) # 100% ok
def consultar_profissionais():
    mensagem = "Consultar"
    profissionais = fun.listar_tabela("profissional")
    return render_template("consulta.html", msg = mensagem, lista=profissionais)


@app.route("/consultar-pacientes", methods=["POST"]) # 100% ok
def consultar_pacientes():
    mensagem = "Consultar"
    pacientes = fun.listar_tabela("pacientes")
    return render_template("consulta.html", msg = mensagem, lista=pacientes)


@app.route("/atualizar", methods=["POST"]) # 100% ok
def atualizar():
    mensagem = "Atualizar"
    return render_template("atualizar.html", msg = mensagem)


@app.route("/atualizar-hospitais", methods=["POST", "GET"]) # 100% ok
def atualizar_hospitais():
    if request.method == 'POST':

        nome = request.form['id_hospital']
        endereco = request.form['endereco']
        especialidade = request.form['especialidade']
        validar_h = fun.validar_campo(nome, 'hospital', 'id_hospital')

        if len(validar_h) > 0:  # existe?
            if fun.teste_try(endereco) > 0 and len(endereco) > 1 and fun.endereco_certo(endereco) > 0:  # se NÃO houver o endereco JÁ cadastrado
                if fun.teste_try(especialidade) > 0 and len(especialidade) > 1:  # se NÃO houver o endereco JÁ cadastrado

                    con = sql.connect("banco\database.db")
                    cur = con.cursor()
                    cur.execute("update hospital SET endereco = '%s', especialidade = '%s' where nome = '%s'" %
                                (endereco, especialidade, nome))
                    con.commit()
                    mensagem = "Hospital atualizado"
                    return render_template("atualizar.html", msg = mensagem)

                else:  # se HOUVER o msm endereço >> mostra o erro
                    mensagem = "Especialidade invalida, tente novamente ou consulte os dados cadastrados"
                    return render_template("error.html", msg=mensagem, dados=especialidade)
            else: # se HOUVER o msm endereço >> mostra o erro
                mensagem = "Endereco invalido, tente novamente ou consulte os dados cadastrados"
                return render_template("error.html", msg=mensagem, dados=endereco)
        else: # se houver o msm nome> mostra o erro
            mensagem = "ID de Hospital invalido, tente novamente ou consulte os dados cadastrados"
            return render_template("error.html", msg=mensagem, dados=nome) # OK - 100%


@app.route("/atualizar-profissionais", methods=["POST","GET"]) # 100% ok
def atualizar_profissionais():
    if request.method == 'POST':
        nome = request.form['nome_pro']
        local_trabalho = request.form['local_trabalho']
        cargo = request.form['cargo']
        salario = request.form['salario']
        cpf = request.form['cpf']
        email = request.form['email']
        telefone = request.form['telefone']

        if len(fun.validar_campo(local_trabalho, 'hospital', 'id_hospital')) > 0 and fun.teste_try(local_trabalho) < 10:  # se hospital existir
            if len(fun.validar_campo(cpf, 'profissional', 'cpf')) == 1 and fun.teste_try(cpf) < 10 and len(cpf) >= 6 and len(cpf) <= 11:  # SE CPF UNICO
                if fun.teste_try(salario) < 10 and int(salario) >= 1212 and int(salario) <= 100000:
                    if fun.teste_try(telefone) < 10 and len(telefone) >= 10 and len(telefone) <= 11:
                        if fun.email_certo(email) > 0:
                            if fun.validar_nome(nome) > 0:
                                if fun.teste_try(cargo) > 0 and len(cargo) > 1:

                                    con = sql.connect("banco\database.db")
                                    cur = con.cursor()
                                    cur.execute(
                                        "update profissional SET nome = '%s', local_trabalho = '%s', cargo = '%s', salario = '%s', email = '%s', telefone = '%s' where cpf = '%s'"
                                        % (nome, local_trabalho, cargo, salario, email, telefone, cpf))
                                    con.commit()
                                    mensagem = "Profissional Atualizado"
                                    return render_template("atualizar.html", msg=mensagem)

                                else:  # se cargo invalido mostra o erro
                                    mensagem = "Cargo invalido, tente novamente ou consulte os dados cadastrados"
                                    return render_template("error.html", msg=mensagem, dados=cargo)
                            else:  # se nome invalido mostra o erro
                                mensagem = "Nome invalido, tente novamente ou consulte os dados cadastrados"
                                return render_template("error.html", msg=mensagem, dados=nome)
                        else:  # se email invalido mostra o erro
                            mensagem = "Email invalido, tente novamente ou consulte os dados cadastrados"
                            return render_template("error.html", msg=mensagem, dados=email)
                    else:  # se telefone invalido mostra o erro
                        mensagem = "Telefone Invalido, tente novamente ou consulte os dados cadastrados"
                        return render_template("error.html", msg=mensagem, dados=telefone)
                else:  # se salario invalido > mostra o erro
                    mensagem = "Salario Invalido!, tente novamente ou consulte os dados cadastrados"
                    return render_template("error.html", msg=mensagem, dados=salario)
            else:  # se CPF invalido > mostra o erro
                mensagem = "CPF Invalido, tente novamente ou consulte os dados cadastrados"
                return render_template("error.html", msg=mensagem, dados=cpf)
        else: # se Não houver o hospital > mostra o erro
            mensagem = "ID de Hospital Invalido, tente novamente ou consulte os dados cadastrados"
            return render_template("error.html", msg=mensagem, dados=local_trabalho) # OK - 100%


@app.route("/atualizar-pacientes", methods=["POST", "GET"]) # 100% ok
def atualizar_pacientes():
    if request.method == 'POST':

        nome = request.form['nome_paciente']
        local_internado = request.form['local_internado']
        profissional_responsavel = request.form['profissional']
        doenca = request.form['doenca']
        cpf = request.form['cpf_paciente']
        email = request.form['email_paciente']
        telefone = request.form['telefone_paciente']

        validar_h = fun.validar_campo(local_internado, 'hospital', 'id_hospital')

        if len(validar_h) > 0 and fun.teste_try(local_internado) < 10:  # se hospital existe
            validar_cpf = fun.validar_campo(cpf, 'pacientes', 'cpf')
            if len(validar_cpf) == 1 and fun.teste_try(cpf) < 10 and len(cpf) >= 6 and len(cpf) <= 11:
                validar_profissional = fun.validar_campo(profissional_responsavel, 'profissional', 'id_profissional')
                if fun.teste_try(profissional_responsavel) < 10 and len(validar_profissional) > 0:
                    if fun.teste_try(telefone) < 10 and len(telefone) >= 10 and len(telefone) <= 11:
                        if fun.email_certo(email) > 0:
                            if fun.validar_nome(nome) > 0:
                                if fun.teste_try(doenca) > 0 and len(doenca) > 1:

                                    con = sql.connect("banco\database.db")
                                    cur = con.cursor()
                                    cur.execute(
                                        "update pacientes SET nome = '%s', local_internado = '%s', profissional_responsavel = '%s', doenca = '%s', email = '%s', telefone = '%s' where cpf = '%s'"
                                        % (nome, local_internado, profissional_responsavel, doenca, email, telefone, cpf))
                                    con.commit()
                                    mensagem = "Paciente Atualizado"
                                    return render_template("atualizar.html", msg=mensagem)

                                else:  # se nome invalido mostra o erro
                                    mensagem = "Patologia invalida, tente novamente ou consulte os dados cadastrados"
                                    return render_template("error.html", msg=mensagem, dados=doenca)
                            else:  # se nome invalido mostra o erro
                                mensagem = "Nome invalido, tente novamente ou consulte os dados cadastrados"
                                return render_template("error.html", msg=mensagem, dados=nome)
                        else:  # se telefone invalido mostra o erro
                            mensagem = "Email invalido, tente novamente ou consulte os dados cadastrados"
                            return render_template("error.html", msg=mensagem, dados=email)
                    else:  # se telefone invalido mostra o erro
                        mensagem = "Telefone Invalido, tente novamente ou consulte os dados cadastrados"
                        return render_template("error.html", msg=mensagem, dados=telefone)
                else:  # se ID de profissional invalido > mostra o erro
                    mensagem = "Id de profissional invalido, tente novamente ou consulte os dados cadastrados"
                    return render_template("error.html", msg=mensagem, dados=profissional_responsavel)
            else:  # se CPF invalido > mostra o erro
                mensagem = "CPF Invalido, tente novamente ou consulte os dados cadastrados"
                return render_template("error.html", msg=mensagem, dados=cpf)
        else: # se Não houver o hospital > mostra o erro
            mensagem = "ID de Hospital Invalido, tente novamente ou consulte os dados cadastrados"
            return render_template("error.html", msg=mensagem, dados=local_internado)# OK - 100%


@app.route("/remover", methods=["POST"]) # 100% ok
def remover():
    mensagem = "Remover"
    return render_template("remocao.html", msg = mensagem)


@app.route("/remover-hospitais", methods=["POST"])
def remover_hospitais():
    # conex_sel = conex_c.execute("delete from %s where %s = '%s'" % (tabela, campo_palavra, palavra))
    if request.method == 'POST':
        id = request.form['nome']
        validar_h = fun.validar_campo(id, 'hospital', 'id_hospital')

        if len(validar_h) > 0 and fun.teste_try(id) < 10:
            con = sql.connect("banco\database.db")
            cur = con.cursor()
            cur.execute("delete from pacientes where local_internado = '%s'" % id)
            cur.execute("delete from profissional where local_trabalho = '%s'" % id)
            cur.execute("delete from hospital where id_hospital = '%s'" % id)
            con.commit()
            mensagem = "Hospital Removido"
            return render_template("remocao.html", msg = mensagem)
        else:  # se Não houver o hospital > mostra o erro
            mensagem = "ID de Hospital Não Existe ou Invalido, tente novamente ou consulte os dados cadastrados"
            return render_template("error.html", msg=mensagem, dados=id)


@app.route("/remover-profissionais", methods=["POST"])
def remover_profissionais():
    if request.method == 'POST':
        cpf = request.form['cpf']

        validar_cpf = fun.validar_campo(cpf, 'profissional', 'cpf')

        if len(validar_cpf) > 0 and fun.teste_try(cpf) < 10:
            con = sql.connect("banco\database.db")
            cur = con.cursor()
            cur.execute("delete from pacientes where profissional_responsavel = '%s'" % validar_cpf[0][0])
            cur.execute("delete from profissional where cpf = '%s'" % cpf)
            con.commit()
            mensagem = "Profissional Removido"
            return render_template("remocao.html", msg=mensagem)

        else:  # se Não houver o hospital > mostra o erro
            mensagem = "CPF de Profissional Não Existe ou Invalido, tente novamente ou consulte os dados cadastrados"
            return render_template("error.html", msg=mensagem, dados=cpf)


@app.route("/remover-pacientes", methods=["POST"])
def remover_pacientes():
    if request.method == 'POST':
        cpf = request.form['cpf_paciente']

        validar_cpf = fun.validar_campo(cpf, 'pacientes', 'cpf')
        if len(validar_cpf) > 0 and fun.teste_try(cpf) < 10:
            con = sql.connect("banco\database.db")
            cur = con.cursor()
            cur.execute("delete from pacientes where cpf = '%s'" % cpf)
            con.commit()
            mensagem = "Paciente Removido"
            return render_template("remocao.html", msg = mensagem)
        else:  # se Não houver o hospital > mostra o erro
            mensagem = "CPF de Paciente Não Existe ou Invalido, tente novamente ou consulte os dados cadastrados"
            return render_template("error.html", msg=mensagem, dados=cpf)


if __name__ =="__main__":
    app.secret_key = "admin123"
    app.run(debug=True)



####################################################################################
        4  SOBRE O RESULTADO

    Com a execução correta deste projeto, será aberto o servidor web com apágina inicial
    apresentando as opções da CRUD, da qual para cada opção será apresentado e direcionado
    para a página correspondente, das quais fornecem instruções para o uso do sistema. Sendo
    possivel inserir dados nas tabelas, consultar, alterar e deletar. Os dados foram coletados 
    do usuário via formulário e usado botões para definir as ações e direcionamentos, no 
    arquivo do servidor, tais dados foram coletados e manejados conforme a opção escolhida 
    do usuário. Sendo feito verificações e direcionamento para a página de erro, quando
   o usuário insere um dado inválido. Contudo, maiores estudos sobre meios
    eficientes de coletar informações do usuário.