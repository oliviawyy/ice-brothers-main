from flask import Flask, render_template, session, redirect, request, jsonify
from model.login import Login
from model.produtos import recuperar_produto_por_codigo
from model.produtos import recuperar_produ
from database.conexao import Conexao

app = Flask(__name__)
app.secret_key = "ice_brothers"


@app.route("/")
def pagina_principal():
    produtos = recuperar_produ()
    return render_template("index.html", produto = produtos)


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logar", methods=["POST", "GET"])
def pag_logar():

    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    usuario_logado = Login.login_usuario(usuario, senha)

    if usuario_logado:

        session["logado"] = True
        session["usuario"] = usuario

        return redirect("/")

    return redirect("/login")

@app.route("/cadastro", methods=["POST", "GET"])
def pag_cadastro():
    return render_template("cadastro.html")




@app.route('/produto/<int:id_produto>')
def pag_produto(id_produto):
    conexao, cursor = Conexao.conectar()
    
    # Busca o produto no banco de dados
    cursor.execute("SELECT * FROM produtos WHERE codigo = %s", (id_produto,))
    produto_carregado = cursor.fetchone()
    
    conexao.close()
    
    if not produto_carregado:
        return "Produto não encontrado no banco de dados!", 404
        
    produto_formatado = {
        'codigo': produto_carregado['codigo'],
        'nome': produto_carregado['nome'],
        'descricao': produto_carregado['descricao'],
        'valor': float(produto_carregado['valor']),
        'foto': produto_carregado['foto'],
        'categoria': produto_carregado['categoria']
    }
        
    # Envia o produto certinho para o HTML
    return render_template("pagina_produto.html", produto=produto_formatado)

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
                'codigo': produto['codigo'],
                'nome': produto['nome'],
                'valor': float(produto['valor']),
                'foto': produto['foto'],
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
    tamanho = request.form.get('tamanho', 'M') # pega o tamanho selecionado (padrão: M
    
    carrinho_sessao = session.get('carrinho', [])
    
    # Verifica se o produto já existe no carrinho com o mesmo tamanho
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


# atualizar quantidafe (+ ou -) 
@app.route('/carrinho/atualizar/<int:codigo>/<string:tamanho>', methods=['POST'])
def atualizar_carrinho(codigo, tamanho):
    acao = request.form.get('acao')
    carrinho_sessao = session.get('carrinho', [])
    
    for item in carrinho_sessao:
        if item['codigo'] == codigo and item['tamanho'] == tamanho:
            if acao == 'aumentar':
                item['quantidade'] += 1
            elif acao == 'diminuir':
                item['quantidade'] -= 1
            break
            
    # Remove itens com quantidade zero ou menor
    carrinho_sessao = [item for item in carrinho_sessao if item['quantidade'] > 0]
    
    session['carrinho'] = carrinho_sessao
    session.modified = True
    return redirect('/carrinho')


# dleter item carro
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


@app.route("/sair")
def sair():
    
    session.clear()
    
    return redirect("/")

@app.route('/colecao/moletom')
def pag_moletom():
    conexao, cursor = Conexao.conectar()
    cursor.execute("SELECT * FROM produtos WHERE categoria = 'MOLETOM'")
    produtos_banco = cursor.fetchall()
    
    conexao.close()
    lista_moletons = []
    for prod in produtos_banco:
        if isinstance(prod, dict):
            lista_moletons.append({
                'codigo': prod.get('codigo') or prod.get('id'), # use o nome real da sua coluna de ID
                'nome': prod.get('nome'),
                'descricao': prod.get('descricao'),
                'valor': float(prod.get('valor')),
                'foto': prod.get('foto'),
                'categoria': prod.get('categoria')
            })
        else:
            lista_moletons.append({
                'codigo': prod[0],
                'nome': prod[1],
                'descricao': prod[2],
                'valor': float(prod[3]),
                'foto': prod[4],
                'categoria': prod[5]
            })
        
    return render_template("moletom.html", produtos=lista_moletons)

if __name__ == '__main__':
    app.run(debug=True)