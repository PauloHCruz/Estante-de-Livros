from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    livros = [
        {"imagem":"https://m.media-amazon.com/images/I/91jCDEyM3fL.jpg", "titulo":"Titulo", "autor": "Autor"},
        {"imagem":"https://m.media-amazon.com/images/I/91jCDEyM3fL.jpg", "titulo":"Titulo", "autor": "Autor"},
        {"imagem":"https://m.media-amazon.com/images/I/91jCDEyM3fL.jpg", "titulo":"Titulo", "autor": "Autor"},
        {"imagem":"https://m.media-amazon.com/images/I/91jCDEyM3fL.jpg", "titulo":"Titulo", "autor": "Autor"},
        {"imagem": "https://m.media-amazon.com/images/I/91jCDEyM3fL.jpg", "titulo": "Titulo", "autor": "Autor"},
        {"imagem": "https://m.media-amazon.com/images/I/91jCDEyM3fL.jpg", "titulo": "Titulo", "autor": "Autor"},
        {"imagem": "https://m.media-amazon.com/images/I/91jCDEyM3fL.jpg", "titulo": "Titulo", "autor": "Autor"},
        {"imagem": "https://m.media-amazon.com/images/I/91jCDEyM3fL.jpg", "titulo": "Titulo", "autor": "Autor"}
    ]
    return render_template('livros.html',livros=livros)

@app.route('/minha-estante')
def minha_estante():
    return render_template('minha-estante.html')

if __name__ == '__main__':
    app.run(debug=True)