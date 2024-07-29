from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(content="<h1>Routing Implementation in Flask</h1>")
    return render_template('index.html')

@app.route('/about')
def about():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(content="<h1>About page</h1>")
    return render_template('index.html')

@app.route('/contact')
def contact():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(content="<h1>Contact page</h1>")
    return render_template('index.html')

@app.route('/user/<username>')
def show_user_profile(username):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(content=f"<h1>Hello, <b>{username}!!</b></h1>")
    return render_template('index.html')

@app.route('/portfolio')
def portfolio_index():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(content='<h1>Rohit Chess</h1>')
    return render_template('index.html')

@app.route('/portfolio/about')
def portfolio_about():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(content="<h1>I'm a Python Full Stack Developer</h1>")
    return render_template('index.html')

@app.route('/portfolio/education')
def education():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(content="<h1>I'm pursuing Artificial Intelligence and Data Science</h1>")
    return render_template('index.html')

@app.route('/portfolio/personal')
def personal():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(content='<h1>Chess Player and Pianist</h1>')
    return render_template('index.html')

@app.route('/portfolio/skills')
def skills():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(content='<h1>Skills: Python, Frontend, Backend, Git, GitHub</h1>')
    return render_template('index.html')

@app.route('/portfolio/achievements')
def achievements():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(content='<h1>I won district chess championship 2 times @2020-2022</h1>')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
