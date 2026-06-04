from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
from collections import Counter

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(
    host="localhost",
    database="lanchonete",
    user="postgres",
    password="12345"
)

cursor = conn.cursor()

# PRODUTOS

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    cursor.execute("SELECT id, nome, descricao, preco, estoque FROM produtos ORDER BY id")
    produtos = cursor.fetchall()

    lista = []
    for p in produtos:
        lista.append({
            "id": p[0],
            "nome": p[1],
            "descricao": p[2],
            "preco": float(p[3]),
            "estoque": p[4]
        })

    return jsonify(lista)


@app.route('/produtos', methods=['POST'])
def cadastrar_produto():
    dados = request.json

    cursor.execute("""
        INSERT INTO produtos (nome, descricao, preco, estoque)
        VALUES (%s, %s, %s, %s)
    """, (
        dados['nome'],
        dados['descricao'],
        dados['preco'],
        dados['estoque']
    ))

    conn.commit()
    return jsonify({"mensagem": "Produto cadastrado"})


@app.route('/produtos/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    dados = request.json

    cursor.execute("""
        UPDATE produtos
        SET nome=%s, descricao=%s, preco=%s, estoque=%s
        WHERE id=%s
    """, (
        dados['nome'],
        dados['descricao'],
        dados['preco'],
        dados['estoque'],
        id
    ))

    conn.commit()
    return jsonify({"mensagem": "Produto atualizado"})


@app.route('/produtos/<int:id>', methods=['DELETE'])
def excluir_produto(id):
    cursor.execute("DELETE FROM produtos WHERE id=%s", (id,))
    conn.commit()

    return jsonify({"mensagem": "Produto excluído"})


# CLIENTES

@app.route('/clientes', methods=['GET'])
def listar_clientes():
    cursor.execute("SELECT * FROM clientes ORDER BY id")
    clientes = cursor.fetchall()

    lista = []
    for c in clientes:
        lista.append({
            "id": c[0],
            "nome": c[1],
            "telefone": c[2],
            "email": c[3]
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
    return jsonify({"mensagem": "Cliente cadastrado"})


@app.route('/clientes/<int:id>', methods=['PUT'])
def atualizar_cliente(id):
    dados = request.json

    cursor.execute("""
        UPDATE clientes
        SET nome=%s, telefone=%s, email=%s
        WHERE id=%s
    """, (
        dados['nome'],
        dados['telefone'],
        dados['email'],
        id
    ))

    conn.commit()
    return jsonify({"mensagem": "Cliente atualizado"})


@app.route('/clientes/<int:id>', methods=['DELETE'])
def excluir_cliente(id):
    cursor.execute("DELETE FROM clientes WHERE id=%s", (id,))
    conn.commit()

    return jsonify({"mensagem": "Cliente excluído"})


# PEDIDOS

@app.route('/pedidos', methods=['GET'])
def listar_pedidos():
    cursor.execute("SELECT * FROM pedidos ORDER BY id DESC")
    pedidos = cursor.fetchall()

    lista = []
    for p in pedidos:
        lista.append({
            "id": p[0],
            "cliente_id": p[1],
            "produtos": p[2],
            "total": float(p[3])
        })

    return jsonify(lista)


@app.route('/pedidos', methods=['POST'])
def criar_pedido():
    dados = request.json

    cliente_id = dados['cliente_id']
    produtos = dados['produtos']
    total = dados['total']

    lista_produtos = [p.strip() for p in produtos.split(",")]
    quantidade_por_produto = Counter(lista_produtos)

    for nome_produto, quantidade in quantidade_por_produto.items():
        cursor.execute(
            "SELECT estoque FROM produtos WHERE nome=%s",
            (nome_produto,)
        )

        resultado = cursor.fetchone()

        if resultado is None:
            return jsonify({"erro": f"Produto {nome_produto} não encontrado"}), 400

        estoque_atual = resultado[0]

        if estoque_atual < quantidade:
            return jsonify({
                "erro": f"Estoque insuficiente para {nome_produto}"
            }), 400

    for nome_produto, quantidade in quantidade_por_produto.items():
        cursor.execute("""
            UPDATE produtos
            SET estoque = estoque - %s
            WHERE nome = %s
        """, (
            quantidade,
            nome_produto
        ))

    cursor.execute("""
        INSERT INTO pedidos (cliente_id, produtos, total)
        VALUES (%s, %s, %s)
    """, (
        cliente_id,
        produtos,
        total
    ))

    conn.commit()
    return jsonify({"mensagem": "Pedido realizado"})


@app.route('/pedidos/<int:id>', methods=['DELETE'])
def excluir_pedido(id):
    cursor.execute("DELETE FROM pedidos WHERE id=%s", (id,))
    conn.commit()

    return jsonify({"mensagem": "Pedido excluído"})


# RELATÓRIO / DASHBOARD

@app.route('/relatorio', methods=['GET'])
def relatorio():
    cursor.execute("SELECT COUNT(*) FROM produtos")
    total_produtos = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM clientes")
    total_clientes = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM pedidos")
    total_pedidos = cursor.fetchone()[0]

    cursor.execute("SELECT COALESCE(SUM(total), 0) FROM pedidos")
    faturamento = cursor.fetchone()[0]

    return jsonify({
        "total_produtos": total_produtos,
        "total_clientes": total_clientes,
        "total_pedidos": total_pedidos,
        "faturamento": float(faturamento)
    })


if __name__ == '__main__':
    app.run(debug=True)