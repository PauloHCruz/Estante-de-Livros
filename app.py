from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('livros.html')

@app.route('/minha-estante')
def minha_estante():
    return render_template('minha-estante.html')

if __name__ == '__main__':
    app.run(debug=True)