from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

def conectar():
    return psycopg2.connect(
        host="localhost",
        database="lanchonete",
        user="postgres",
        password="12345"
    )

# Cadastrar produto
@app.route('/produtos', methods=['POST'])
def cadastrar_produto():
    dados = request.json

    conn = conectar()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO produtos (nome, descricao, preco) VALUES (%s, %s, %s)",
        (dados['nome'], dados['descricao'], dados['preco'])
    )

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"mensagem": "Produto cadastrado com sucesso!"})

# Listar produtos
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("SELECT * FROM produtos ORDER BY id")
    produtos = cur.fetchall()

    lista = []
    for p in produtos:
        lista.append({
            "id": p[0],
            "nome": p[1],
            "descricao": p[2],
            "preco": float(p[3])
        })

    cur.close()
    conn.close()

    return jsonify(lista)

# Excluir produto
@app.route('/produtos/<int:id>', methods=['DELETE'])
def excluir_produto(id):
    conn = conectar()
    cur = conn.cursor()

    cur.execute("DELETE FROM produtos WHERE id = %s", (id,))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"mensagem": "Produto excluído com sucesso!"})

# Atualizar produto
@app.route('/produtos/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    dados = request.json

    conn = conectar()
    cur = conn.cursor()

    cur.execute(
        "UPDATE produtos SET nome=%s, descricao=%s, preco=%s WHERE id=%s",
        (dados['nome'], dados['descricao'], dados['preco'], id)
    )

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"mensagem": "Produto atualizado com sucesso!"})

# Cadastrar cliente
@app.route('/clientes', methods=['POST'])
def cadastrar_cliente():
    dados = request.json

    conn = conectar()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO clientes (nome, telefone, email) VALUES (%s, %s, %s)",
        (dados['nome'], dados['telefone'], dados['email'])
    )

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"mensagem": "Cliente cadastrado com sucesso!"})

# Listar clientes
@app.route('/clientes', methods=['GET'])
def listar_clientes():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("SELECT * FROM clientes ORDER BY id")
    clientes = cur.fetchall()

    lista = []
    for c in clientes:
        lista.append({
            "id": c[0],
            "nome": c[1],
            "telefone": c[2],
            "email": c[3]
        })

    cur.close()
    conn.close()

    return jsonify(lista)

# Excluir cliente
@app.route('/clientes/<int:id>', methods=['DELETE'])
def excluir_cliente(id):
    conn = conectar()
    cur = conn.cursor()

    cur.execute("DELETE FROM clientes WHERE id = %s", (id,))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"mensagem": "Cliente excluído com sucesso!"})

# ✏️ Atualizar cliente
@app.route('/clientes/<int:id>', methods=['PUT'])
def atualizar_cliente(id):
    dados = request.json

    conn = conectar()
    cur = conn.cursor()

    cur.execute(
        "UPDATE clientes SET nome=%s, telefone=%s, email=%s WHERE id=%s",
        (dados['nome'], dados['telefone'], dados['email'], id)
    )

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"mensagem": "Cliente atualizado com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)