from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return 'Hello Welcome to page created by Flask'

@app.route('/about')
def about():
    return 'About Page'

if __name__=='__main__':
    app.run(debug=True)

