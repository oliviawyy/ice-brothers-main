from flask import Flask, render_template, session, redirect, request, jsonify
from model.login import Login
from model.produtos import recuperar_produto_por_codigo
from database.conexao import Conexao

app = Flask(__name__)
app.secret_key = "ice_brothers"


@app.route("/")
def pagina_principal():
     return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logar", methods=["POST", "GET"])
def pag_logar():
     usuario = request.form.get("usuario")
     senha = request.form.get("senha") 

     usuario_logado = Login.login_usuario(usuario, senha)

     if usuario_logado:
          return redirect("/")
     else:
          return render_template("login.html")

@app.route("/cadastro")
def pag_cadastro():
     return render_template("cadastro.html")

# ROTA DINÂMICA DO PRODUTO (Busca qualquer ID da tabela)
@app.route('/produto/<int:id_produto>')
def pag_produto(id_produto):
    conexao, cursor = Conexao.conectar()
    cursor.execute("SELECT * FROM produtos WHERE codigo = %s", (id_produto,))
    produto_carregado = cursor.fetchone()
    conexao.close()
    
    if not produto_carregado:
        return "Produto não encontrado no banco de dados!", 404
        
    return render_template("pagina_produto.html", produto=produto_carregado)

# ROTA PARA EXIBIR O CARRINHO
@app.route('/carrinho')
def ver_carrinho():
    carrinho_sessao = session.get('carrinho', []) 
    subtotal = 0
    itens_carrinho = []
    
    for item in carrinho_sessao:
        produto = recuperar_produto_por_codigo(item['codigo'])
        if produto:
            produto_completo = {
                'codigo': produto[0],
                'nome': produto[1],
                'valor': float(produto[3]),
                'foto': produto[4],
                'tamanho': item['tamanho'],
                'quantidade': item['quantidade']
            }
            subtotal += produto_completo['valor'] * produto_completo['quantidade']
            itens_carrinho.append(produto_completo)
            
    return render_template('carrinho.html', itens_carrinho=itens_carrinho, subtotal=subtotal)

# ROTA PARA ADICIONAR UM ITEM AO CARRINHO
@app.route('/carrinho/adicionar', methods=['POST'])
def adicionar_carrinho():
    codigo = int(request.form.get('produto_codigo'))
    tamanho = request.form.get('tamanho', 'M') # Pega o tamanho do input radio (Padrão: M)
    
    carrinho_sessao = session.get('carrinho', [])
    
    # verifica se o produto já existe no carrinho com o mesmo tamanho, se sim, aumenta a quantidade
    existe = False
    for item in carrinho_sessao:
        if item['codigo'] == codigo and item['tamanho'] == tamanho:
            item['quantidade'] += 1
            existe = True
            break
            
    if not existe:
        carrinho_sessao.append({
            'codigo': codigo,
            'tamanho': tamanho,
            'quantidade': 1
        })
        
    session['carrinho'] = carrinho_sessao
    session.modified = True
    return redirect('/carrinho')

# rota p atualizar + -
@app.route('/carrinho/atualizar/<int:codigo>', methods=['POST'])
def atualizar_carrinho(codigo):
    acao = request.form.get('acao')
    carrinho_sessao = session.get('carrinho', [])
    
    for item in carrinho_sessao:
        if item['codigo'] == codigo:
            if acao == 'aumentar':
                item['quantidade'] += 1
            elif acao == 'diminuir':
                item['quantidade'] -= 1
            break
            
    # remove itens com quantidade zero ou nda
    carrinho_sessao = [item for item in carrinho_sessao if item['quantidade'] > 0]
    
    session['carrinho'] = carrinho_sessao
    session.modified = True
    return redirect('/carrinho')

# rota pra deletar um item no carrinho
@app.route('/carrinho/remover/<int:codigo>/<string:tamanho>')
def remover_carrinho(codigo, tamanho):
    carrinho_sessao = session.get('carrinho', [])
    
    carrinho_sessao = [item for item in carrinho_sessao if not (item['codigo'] == codigo and item['tamanho'] == tamanho)]
    
    session['carrinho'] = carrinho_sessao
    session.modified = True
    return redirect('/carrinho')


@app.route('/limpar-carrinho')
def limpar_carrinho():
    session.pop('carrinho', None)
    return redirect('/')



@app.route('/sobre')
def pagina_sobre():
    return render_template("sobre.html")

if __name__ == '__main__':
     app.run(debug=True)