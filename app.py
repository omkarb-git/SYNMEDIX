# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route("/signup")
# def signup():
#     return render_template('signup.html')

# @app.route("/dashboard")
# def dashboard():
#     return render_template('dashboard.html')

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a random secret key

# Mock user database (replace with a real database in production)
users = {
    'test@example.com': {
        'password': '12',
        'name': 'John Doe'
    }
}

@app.route('/')
def home():
    # Check if user is logged in
    logged_in = 'user_email' in session
    user_name = users[session['user_email']]['name'] if logged_in else None
    return render_template('home.html', logged_in=logged_in, user_name=user_name)

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/signin")
def signin():
    return render_template('signup.html')

# @app.route("/dashboard")
# def dashboard():
#     return render_template("dashboard.html")

@app.route("/dashboard")
def dashboard():
    # Check if user is logged in, if not redirect to signin
    if 'user_email' not in session:
        return redirect(url_for('signin'))
    
    # Get user info from mock database
    user_email = session['user_email']
    user = users.get(user_email, {})
    return render_template('dashboard.html', user=user)

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Check if user exists and password matches
    if email in users and users[email]['password'] == password:
        session['user_email'] = email
        return jsonify({'success': True})
    
    return jsonify({'success': False, 'message': 'Invalid credentials'})

# @app.route('/logout')
# def logout():
#     # Remove user from session
#     session.pop('user_email', None)
#     return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)