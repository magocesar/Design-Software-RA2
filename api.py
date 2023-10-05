from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('homepage.html'), 404

@app.route('/')
def index():
    return render_template('homepage.html', title='Home')

if __name__ == '__main__':
    app.run(debug=True)