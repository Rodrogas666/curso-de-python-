from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def calcularIMC():
    peso = int(request.form['txtPeso'])
    altura = float(request.form['txtAltura'])
    imc = peso / (altura * altura)
    print(imc)

    if imc < 18.5:
        mensaje = "Peso bajo"
    else:
        if imc > 19.5 and imc < 29.9:
            mensaje = "Peso normal"
        else:
            if imc > 29.9:
                mensaje = "Obeso"

    return render_template('index.html', imc=imc, mensaje=mensaje) #El primero es como lo recolecto, el segundo es el dato que envío]

if __name__ == '__main__':
    app.run(debug=True)
