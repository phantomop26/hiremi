from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = ""

users = {'user1': 'password1'}  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        i
    return render_template('login.html')

@app.route('/success')
def success():
    return 'Login Successful!'


if __name__ == '__main__':
    app.run(debug=True)
