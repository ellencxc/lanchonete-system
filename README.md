# Sistema de Lanchonete - AC1

# Descrição do Projeto
A funcionalidade implementada nesta etapa foi o **cadastro e gerenciamento de produtos** da lanchonete, com integração entre frontend, backend e banco de dados.


# AC1
# Cadastro e gerenciamento de produtos
Nesta etapa, o sistema permite:

- Cadastrar produtos
- Listar produtos cadastrados na mesma página
- Exibir os produtos em formato de cards
- Excluir produtos cadastrados
- Armazenar os dados no banco PostgreSQL


# Tecnologias Utilizadas

# Frontend
- HTML
- CSS
- JavaScript

# Backend
- Python
- Flask
- Flask-CORS

# Banco de Dados
- PostgreSQL

# AC2 - Cadastro e gerenciamento de clientes

# Funcionalidades implementadas:

# Clientes
- Cadastrar cliente
- Listar clientes
- Editar cliente
- Excluir cliente

# Produtos (melhoria)
- Editar produto

# Tecnologias utilizadas:
- Frontend: HTML, CSS, JavaScript
- Backend: Python (Flask)
- Banco de dados: PostgreSQL

# Integração:
Sistema totalmente integrado entre frontend, backend e banco de dados, seguindo os princípios do Manifesto Ágil.
# Estrutura do Projeto
 
# AC3- Pedidos

Sistema Full Stack desenvolvido para gerenciamento de uma lanchonete utilizando:

- Frontend: HTML, CSS e JavaScript
- Backend: Python Flask
- Banco de Dados: PostgreSQL


# Funcionalidades

# Produtos
- Cadastrar produtos
- Listar produtos
- Editar produtos
- Excluir produtos
- Exibir imagem do produto

# Clientes
- Cadastrar clientes
- Listar clientes
- Editar clientes
- Excluir clientes

# Pedidos
- Selecionar cliente
- Adicionar produtos ao carrinho
- Remover produtos do carrinho
- Finalizar pedido
- Listar pedidos realizados
- Excluir pedidos realizados

# PROVA

## Funcionalidades

# Produtos
- Cadastrar produtos
- Listar produtos
- Editar produtos
- Excluir produtos

# Clientes
- Cadastrar clientes
- Listar clientes
- Editar clientes
- Excluir clientes

# Pedidos
- Realizar pedidos
- Exibir pedidos realizados
- Excluir pedidos

# Dashboard / Relatórios
- Total de produtos cadastrados
- Total de clientes cadastrados
- Total de pedidos realizados
- Faturamento total

# Controle de Estoque
- Cadastro de quantidade em estoque
- Exibição do estoque disponível
- Atualização automática após vendas
- Bloqueio de vendas quando o estoque é igual a zero


## Banco de Dados

Tabelas utilizadas:

# produtos

- id
- nome
- descricao
- preco
- estoque

# clientes

- id
- nome
- telefone
- email

# pedidos

- id
- cliente_id
- produtos
- total


# Tecnologias Utilizadas

- Python
- Flask
- PostgreSQL
- HTML
- CSS
- JavaScript


```bash
lanchonete-system/
│
├── backend/
│   └── app.py
│
├── frontend/
│   └── index.html
│
├── database/
│   └── schema.sql
│
└── README.md