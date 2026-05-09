from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

# =========================
# CONEXÃO BANCO
# =========================

conn = psycopg2.connect(
    host="localhost",
    database="lanchonete",
    user="postgres",
    password="12345"
)

cursor = conn.cursor()

# =========================
# PRODUTOS
# =========================

@app.route('/produtos', methods=['GET'])
def listar_produtos():

    cursor.execute("SELECT * FROM produtos ORDER BY id")
    produtos = cursor.fetchall()

    lista = []

    for produto in produtos:
        lista.append({
            "id": produto[0],
            "nome": produto[1],
            "descricao": produto[2],
            "preco": float(produto[3])
        })

    return jsonify(lista)


@app.route('/produtos', methods=['POST'])
def cadastrar_produto():

    dados = request.json

    cursor.execute("""
        INSERT INTO produtos (nome, descricao, preco)
        VALUES (%s, %s, %s)
    """, (
        dados['nome'],
        dados['descricao'],
        dados['preco']
    ))

    conn.commit()

    return jsonify({
        "mensagem": "Produto cadastrado"
    })


@app.route('/produtos/<int:id>', methods=['PUT'])
def atualizar_produto(id):

    dados = request.json

    cursor.execute("""
        UPDATE produtos
        SET nome=%s,
            descricao=%s,
            preco=%s
        WHERE id=%s
    """, (
        dados['nome'],
        dados['descricao'],
        dados['preco'],
        id
    ))

    conn.commit()

    return jsonify({
        "mensagem": "Produto atualizado"
    })


@app.route('/produtos/<int:id>', methods=['DELETE'])
def excluir_produto(id):

    cursor.execute(
        "DELETE FROM produtos WHERE id=%s",
        (id,)
    )

    conn.commit()

    return jsonify({
        "mensagem": "Produto excluído"
    })

# =========================
# CLIENTES
# =========================

@app.route('/clientes', methods=['GET'])
def listar_clientes():

    cursor.execute("SELECT * FROM clientes ORDER BY id")
    clientes = cursor.fetchall()

    lista = []

    for cliente in clientes:
        lista.append({
            "id": cliente[0],
            "nome": cliente[1],
            "telefone": cliente[2],
            "email": cliente[3]
        })

    return jsonify(lista)


@app.route('/clientes', methods=['POST'])
def cadastrar_cliente():

    dados = request.json

    cursor.execute("""
        INSERT INTO clientes (nome, telefone, email)
        VALUES (%s, %s, %s)
    """, (
        dados['nome'],
        dados['telefone'],
        dados['email']
    ))

    conn.commit()

    return jsonify({
        "mensagem": "Cliente cadastrado"
    })


@app.route('/clientes/<int:id>', methods=['PUT'])
def atualizar_cliente(id):

    dados = request.json

    cursor.execute("""
        UPDATE clientes
        SET nome=%s,
            telefone=%s,
            email=%s
        WHERE id=%s
    """, (
        dados['nome'],
        dados['telefone'],
        dados['email'],
        id
    ))

    conn.commit()

    return jsonify({
        "mensagem": "Cliente atualizado"
    })


@app.route('/clientes/<int:id>', methods=['DELETE'])
def excluir_cliente(id):

    cursor.execute(
        "DELETE FROM clientes WHERE id=%s",
        (id,)
    )

    conn.commit()

    return jsonify({
        "mensagem": "Cliente excluído"
    })

# =========================
# PEDIDOS
# =========================

@app.route('/pedidos', methods=['GET'])
def listar_pedidos():

    cursor.execute("SELECT * FROM pedidos ORDER BY id DESC")
    pedidos = cursor.fetchall()

    lista = []

    for pedido in pedidos:
        lista.append({
            "id": pedido[0],
            "cliente_id": pedido[1],
            "produtos": pedido[2],
            "total": float(pedido[3])
        })

    return jsonify(lista)


@app.route('/pedidos', methods=['POST'])
def criar_pedido():

    dados = request.json

    cursor.execute("""
        INSERT INTO pedidos (
            cliente_id,
            produtos,
            total
        )
        VALUES (%s, %s, %s)
    """, (
        dados['cliente_id'],
        dados['produtos'],
        dados['total']
    ))

    conn.commit()

    return jsonify({
        "mensagem": "Pedido realizado"
    })


@app.route('/pedidos/<int:id>', methods=['DELETE'])
def excluir_pedido(id):

    cursor.execute(
        "DELETE FROM pedidos WHERE id=%s",
        (id,)
    )

    conn.commit()

    return jsonify({
        "mensagem": "Pedido excluído"
    })
    
# START

if __name__ == '__main__':
    app.run(debug=True)