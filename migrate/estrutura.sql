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
('Moletom Shark Camo Blue', 'Casaco camuflado azul estilo tubarão com zíper total até o topo do capuz.', 289.90, 'static/img/tuba_moletom.png', 'MOLETOM'),
('Moletom Hoodie Ice Classic Blue', 'Moletom azul premium com estampa dourada exclusiva dos mascotes Ice Brothers.', 249.90, 'static/img/moletom-azul.png', 'MOLETOM'),
('Moletom Hoodie Mind-Blowing White', 'Moletom branco puro com estampa centralizada streetwear clássica.', 229.90, 'static/img/moletom-branco.png', 'MOLETOM'),
('Moletom Hoodie Tie-Dye Dark Ice', 'Estampa estilo tie-dye sombrio com os mascotes de cubo de gelo destacados.', 259.90, 'static/img/moletom-preto.webp', 'MOLETOM'),
('Jaqueta Puffer Frostbite Fur', 'Casaco puffer acolchoado azul glacial com capuz peludo para frio extremo.', 349.90, 'static/img/puffer.png', 'MOLETOM'),
('Conjunto Cropped Bear Street', 'Conjunto moletom preto com detalhes de corrente cravejada e mascote urso polar.', 299.90, 'static/img/conjunto_moletom.png', 'MOLETOM');
    

CREATE TABLE IF NOT EXISTS comentarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produto_codigo VARCHAR(50) NOT NULL,
    usuario VARCHAR(100) NOT NULL,
    texto TEXT NOT NULL
);
