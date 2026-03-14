from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(
    database="lanchonete",
    user="postgres",
    password="12345",
    host="localhost",
    port="5432"
)
@app.route("/")
def home():
    return "API da Lanchonete funcionando!"

@app.route("/produtos", methods=["POST"])
def criar_produto():

    data = request.json

    nome = data["nome"]
    descricao = data["descricao"]
    preco = data["preco"]

    cur = conn.cursor()

    cur.execute(
        "INSERT INTO produtos (nome, descricao, preco) VALUES (%s,%s,%s)",
        (nome, descricao, preco)
    )

    conn.commit()

    return jsonify({"mensagem": "Produto cadastrado com sucesso"})

@app.route("/produtos", methods=["GET"])
def listar_produtos():

    cur = conn.cursor()
    cur.execute("SELECT * FROM produtos")

    produtos = cur.fetchall()

    lista = []

    for p in produtos:
        lista.append({
            "id": p[0],
            "nome": p[1],
            "descricao": p[2],
            "preco": float(p[3])
        })

    return jsonify(lista)
@app.route("/produtos/<int:id>", methods=["DELETE"])
def deletar_produto(id):

    cur = conn.cursor()

    cur.execute("DELETE FROM produtos WHERE id = %s", (id,))

    conn.commit()

    return jsonify({"mensagem": "Produto deletado com sucesso"})
if __name__ == "__main__":
    app.run(debug=True)