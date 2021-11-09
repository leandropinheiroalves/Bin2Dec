from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/resultado', methods=['POST'])
def resultado():
    binario = ''
    erro = ''
    try:
        binario = request.form['binario']
        resp = int(request.form['binario'], 2)
    except ValueError:
        resp = ''
        erro = 'ERRO! O valor digitado só pode conter 0 ou 1!'
    return render_template('resultado.html', resultado=resp, bin=binario, erro=erro)


if __name__ == '__main__':
    app.run(debug=True)
