from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Route 1: Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Route 2: Vintage Car 1
@app.route('/car1')
def car1():
    return render_template('car1.html')

# Route 3: Vintage Car 2
@app.route('/car2')
def car2():
    return render_template('car2.html')

# Route 4: Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route 5: Redirect to Car 1 Page
@app.route('/go-to-car1')
def go_to_car1():
    return redirect(url_for('car1'))

if __name__ == '__main__':
    app.run(debug=True)