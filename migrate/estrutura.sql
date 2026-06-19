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



CREATE TABLE produtos(
    codigo INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nome VARCHAR(350) NOT NULL,
    descricao VARCHAR(500) NOT NULL,
    valor FLOAT,
    foto VARCHAR(350) NOT NULL,
    categoria VARCHAR(100) NOT NULL 
);
    
    
INSERT INTO produtos(nome, descricao, valor, foto, categoria)
VALUES( 'DEEP BLUE', 'Streetwear pesado com estética premium. Tom azul royal intenso com caimento largo (boxy), ombros caídos e gola grossa que não deforma. Postura firme e mente fria.', '130.90', 'static/img/ChatGPT Image 28 de mai. de 2026, 16_35_36.png', 'CAMISAS'),
	  ( 'SKY BLUE', 'Estética clean para o topo do seu visual. Tom azul claro moderno em tecido de alta gramatura, garantindo a estrutura perfeita das marcas de gringa com máximo conforto.', '139.90', 'static/img/ChatGPT Image 28 de mai. de 2026, 16_36_39.png', 'CAMISAS'),
      ( 'ICE WHITE', 'O clássico indispensável que manda no jogo. Base branca impecável com alto contraste no logo. Ultra versátil, combina perfeitamente com correntes e acessórios.', '139.90', 'static/img/over_branca.png', 'CAMISAS');
INSERT INTO produtos (nome, descricao, valor, foto, categoria) VALUES 
('Moletom Oversized Ice Classic', 'Moletom premium 100% algodão, modelagem oversized com estampa minimalista.', 199.90, 'static/img/moletom-classic.jpg', 'MOLETOM'),
('Moletom Hoodie Street Aura', 'Moletom com capuz ajustável, bolso canguru e estampa nas costas. Estilo urbano puro.', 249.90, 'static/img/moletom-aura.jpg', 'MOLETOM'),
('Moletom Crewneck Frostbite', 'Gola careca, tecido pesado e interior flanelado. Conforto máximo para os dias frios.', 189.90, 'static/img/moletom-frost.jpg', 'MOLETOM');
    