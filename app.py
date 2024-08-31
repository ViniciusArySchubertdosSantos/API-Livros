# 1. Objetivo - Criar um API que disponibiliza a consulta, criaçao, ediçao e exclsão de livros
# 2. URL base - localhost
# 3. Endpoints - 
    
    # - localhost/livros(GET)
    # - localhost/livros(POST)
    # - localhost/livros/id(GET)
    # - localhost/livro/id(PUT)
    # - locashost/livro/id(DELETE)



# 4. Quais recursos - Livros 

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id' : 1,
        'título': 'O senhor dos anéis - A sociedade do Anel',
        'autor': 'J.R.R Tolkien',
    },
    
    {
        'id' : 2,
        'título': 'A Arte da Guerra: Os treze capítulos completos',
        'autor': ' Sun Tzu ',
    },
    {
        'id' : 3,
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.k howling',
    },
]

   

@app.route('/livros', methods=['GET'])
def obter_livros():
    
    return jsonify(livros)


@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            
            return jsonify(livro)


@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            
            return jsonify(livros[indice])


@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
   novo_livro = request.get_json()
   livros.append(novo_livro)
   
   return jsonify(livros)


@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
        
        return jsonify(livros)




app.run(port=5000,host='localhost',debug=True)