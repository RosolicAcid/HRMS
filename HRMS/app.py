from flask import Flask, render_template

app = Flask(__name__)

@app.route('/employee_profile')
def employee_profile():
    return render_template('employee_profile.html')

@app.route('/')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
