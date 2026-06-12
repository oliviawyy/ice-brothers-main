CREATE DATABASE IF NOT EXISTS ice_brothers;

USE ice_brothers;

CREATE TABLE IF NOT EXISTS usuarios(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(200) NOT NULL,
    endereco VARCHAR(300) NOT NULL, 
    CEP VARCHAR(8) NOT NULL,
	senha VARCHAR(100) NOT NULL
    );

INSERT INTO usuarios (nome, email, endereco, CEP, senha)
VALUES ('Ana', 'ana.machioni@aluno.senai.br', 'rua oliveira castro 77','77733310','777' );
