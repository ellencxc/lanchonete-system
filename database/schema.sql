CREATE DATABASE lanchonete;

CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    descricao TEXT,
    preco DECIMAL
);