/*
####################################################################################
# TITULO do arquivo: script.sql
# AUTOR: Iara de Melo Dantas Bezerra
# Data: 25/11/222 | PERIODO: 2022.2  | PROJETO: Completo | Versão: 0.2
# OBJETIVO DESSE ARQUIVO: criar as tabelasdo projeto
####################################################################################
*/

drop table hospital;
--drop table profissional
--drop table pacientes


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

-- Permite a visualização dos campos das tabelas
select * from hospital;
select * from profissional;
select * from pacientes;

--select * from hospital where nome = 'Hospital da Fe';
