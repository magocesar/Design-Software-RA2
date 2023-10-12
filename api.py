from flask import Flask, render_template, request, redirect, session
from python_proj import Commun, Cliente, Login

app = Flask(__name__, template_folder='templates')

@app.errorhandler(404)
def page_not_found(e):

    if session.get('log') == False or None:
        return redirect('/signin')
    
    return redirect('/homepage/1')
    
@app.route('/')
def index():

    if session.get('log') == False or None:
        return redirect('/signin')

    return redirect('/homepage/1')

@app.route('/homepage/<cp>', methods=['GET'])
def homepage(cp):

    if session.get('log') == False or None:
        return redirect('/signin')

    cp = int(cp)

    if cp < 1:
        cp = 1
    
    numberOfPages = Commun.Commun.calcHomepagePages()

    if cp > numberOfPages:
        cp = numberOfPages

    resultQuery = Commun.Commun.HomepageQueryInit(cp)
    
    return render_template('homepage.html', currentPage=cp, numberOfPages=numberOfPages, resultQuery=resultQuery)

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/login', methods=['POST'])
def login():

    if request.method != 'POST':
        return redirect('/signin')
    
    login = request.form['login']
    senha = request.form['senha']

    login = Login.Login(login, senha)

    if login.getAutenticado():
        session['log'] = True
        session['id'] = login.id
        return redirect('/homepage/1')
    else:
        return redirect('/signin')

@app.route('/logout')
def logout():
    session['log'] = False
    session['id'] = None
    return redirect('/signin')

@app.route('/novocliente')
def novocliente():

    if session.get('log') == False or None:
        return redirect('/signin')

    return render_template('novocliente.html')

@app.route('/search', methods=['GET', 'POST'])
def busca():

    if session.get('log') == False or None:
        return redirect('/signin')
    
    if request.method == 'POST':
        if request.form['search'] != None:
            search = request.form['search']
        else:
            return redirect('/homepage/1')
    else:
        return redirect('/homepage/1')
            
    resultQuery = Commun.Commun.SearchQueryInit(search)

    return render_template('search.html', resultQuery=resultQuery, search=search)

@app.route('/cliente/<id>')
def cliente(id):

    if session.get('log') == False or None:
        return redirect('/signin')

    cliente = Cliente.Cliente.getFromId(id)

    return render_template('cliente.html', cliente=cliente)

if __name__ == '__main__':
    app.secret_key = "super secret key"
    app.run(debug=True)
