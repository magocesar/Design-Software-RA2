from flask import Flask, render_template, request, redirect, session
from python_proj import Commun
app = Flask(__name__, template_folder='templates')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('homepage.html'), 404

@app.route('/homepage', methods=['GET'])
def homepage():

    currentPage = 1

    if request.args.get('page') != None:
        currentPage = int(request.args.get('page'))

    if currentPage < 1:
        currentPage = 1
    
    numberOfPages = Commun.Commun.calcHomepagePages()

    if currentPage > numberOfPages:
        currentPage = numberOfPages

    resultQuery = Commun.Commun.HomepageQueryInit(currentPage)
    
    return render_template('homepage.html', currentPage=currentPage, numberOfPages=numberOfPages, resultQuery=resultQuery)

@app.route('/signin')
def signin():
    return render_template('signin.html', title='Sign In')

@app.route('/novocliente')
def novocliente():
    return render_template('novocliente.html', title='Novo Cliente')

@app.route('/search', methods=['GET', 'POST'])
def busca():
    
    if request.method == 'POST':
        if request.form['search'] != None:
            search = request.form['search']
        else:
            return redirect('/homepage')
    else:
        return redirect('/homepage')
            
    resultQuery = Commun.Commun.SearchQueryInit(search)

    return render_template('search.html', resultQuery=resultQuery, search=search)

if __name__ == '__main__':
    app.run(debug=True)
