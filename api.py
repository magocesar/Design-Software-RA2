from flask import Flask, render_template, request, redirect, session
from python_proj import Homepage
app = Flask(__name__, template_folder='templates')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 404

@app.route('/homepage', methods=['GET'])
def homepage():

    if request.args.get('page') != None:
        currentPage = int(request.args.get('page'))
    else:
        currentPage = 1

    if currentPage < 1:
        currentPage = 1
    
    numberOfPages = Homepage.Homepage.calculateTotalPages()

    if currentPage > numberOfPages:
        currentPage = numberOfPages

    resultQuery = Homepage.Homepage.selectClient(currentPage)
    
    return render_template('homepage.html', currentPage=currentPage, numberOfPages=numberOfPages, resultQuery=resultQuery)

@app.route('/signin')
def signin():
    return render_template('signin.html', title='Sign In')

@app.route('/novocliente')
def novocliente():
    return render_template('novocliente.html', title='Novo Cliente')

@app.route('/search')
def busca():
    return render_template('search.html', title='Busca')

if __name__ == '__main__':
    app.run(debug=True)
