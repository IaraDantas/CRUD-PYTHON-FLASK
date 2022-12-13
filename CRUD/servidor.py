####################################################################################
# TITULO do arquivo python: servidor.py
# AUTOR: Iara de Melo Dantas Bezerra | iaradantasredes@gmail.com
# Data: 25/11/222 | PERIODO: 2022.2  | PROJETO: Completo | Versão: 0.2
# OBJETIVO DESSE ARQUIVO: Criar o web service com flask e aplicar a CRUD.
####################################################################################

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
