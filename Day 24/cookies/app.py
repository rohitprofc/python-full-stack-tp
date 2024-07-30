from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')
        user_name = request.form.get('user_name')
        existing_name = request.cookies.get('user_name')

        if action == 'Set Cookie':
            if existing_name == user_name:
                message = f"Welcome back, {user_name}!"
            else:
                message = f"Hello, {user_name}!"
                resp = make_response(render_template('index.html', message=message, form_visible=False))
                resp.set_cookie('user_name', user_name)
                return resp
        
        elif action == 'Clear Cookie':
            resp = make_response(render_template('index.html', message="Cookie cleared. Please enter your name again.", form_visible=True))
            resp.set_cookie('user_name', '', expires=0)  # Clear the cookie
            return resp

    # Handle GET requests
    user_name = request.cookies.get('user_name')
    if user_name:
        message = f"Welcome back, {user_name}!"
        form_visible = True
    else:
        message = "Please enter your name to set a cookie."
        form_visible = True

    return render_template('index.html', message=message, form_visible=form_visible)

if __name__ == '__main__':
    app.run(debug=True)
