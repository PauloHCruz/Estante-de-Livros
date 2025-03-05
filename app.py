from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "chave_super_secreta"

livros = [
    {"id": "1", "titulo": "Flask Web Development", "autor": "Miguel Grinberg", "imagem": "https://m.media-amazon.com/images/I/91jCDEyM3fL.jpg"},
    {"id": "2", "titulo": "Flask Web Development", "autor": "Miguel Grinberg", "imagem": "https://m.media-amazon.com/images/I/91jCDEyM3fL.jpg"},
    {"id": "3", "titulo": "Flask Web Development", "autor": "Miguel Grinberg", "imagem": "https://m.media-amazon.com/images/I/91jCDEyM3fL.jpg"}
]

@app.route("/")
def home():
    minha_estante = session.get("minha_estante", {})
    return render_template("livros.html", livros=livros, minha_estante=minha_estante)

@app.route("/minha-estante")
def minha_estante():
    minha_estante = session.get("minha_estante", {})
    livros_na_estante = [livro for livro in livros if livro["id"] in minha_estante]
    return render_template("minha-estante.html", livros=livros_na_estante, minha_estante=minha_estante)

@app.route("/alterna_estante", methods=["POST"])
def alterna_estante():
    book_id = request.form.get("book_id")
    minha_estante = session.get("minha_estante", {})

    if book_id in minha_estante:
        del minha_estante[book_id]
    else:
        minha_estante[book_id] = "quero ler"

    session["minha_estante"] = minha_estante
    session.modified = True

    return redirect(request.referrer or url_for("home"))

@app.route("/atualiza_status", methods=["POST"])
def atualiza_status():
    book_id = request.form.get("book_id")
    status = request.form.get("status")
    minha_estante = session.get("minha_estante", {})

    if book_id in minha_estante:
        minha_estante[book_id] = status

    session["minha_estante"] = minha_estante
    session.modified = True

    return redirect(request.referrer or url_for("minha_estante"))

if __name__ == "__main__":
    app.run(debug=True)