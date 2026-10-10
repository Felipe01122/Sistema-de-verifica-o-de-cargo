from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'a'

usuarios = {



    "01": {
        "cargo":"admin",
        "nome":"roger",
        "id":"01",
    },



    "02": {
            "cargo":"gerente",
            "nome":"ana",
            "id":"02",
    },


    "03": {
            "cargo":"operador",
            "nome":"pedro",
            "id":"03",
    }
}



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index', methods = ['POST'] )
def acesso():
    dados = request.get_json()

    id_funcionario = dados.get('id')
    nome = dados.get('nome')
    
    usuario = usuarios.get(id_funcionario)
    

    if usuario and usuario['nome'] == nome and usuario['id'] == id_funcionario:
        session['nome'] = usuario['nome']
        session['cargo'] = usuario['cargo']
        session['id'] = usuario['id']
        return jsonify({"sucesso": True,
        "mensagem":"Acesso liberado",
        "funcionario":usuario})
    else:
        return jsonify({"sucesso": False,
        "mensagem":"Acesso negado"})

@app.route('/painel')
def painel():
    return render_template('painel.html',
    nome = session.get('nome'),
    cargo = session.get('cargo'),
    id = session.get('id')
    )

if __name__ == '__main__':
    app.run(debug=True)