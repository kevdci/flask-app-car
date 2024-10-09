from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')  # Should render home.html

@app.route('/car1')
def car1():
    return render_template('car1.html')

@app.route('/car2')
def car2():
    return render_template('car2.html')  # Should render car2.html

@app.route('/contact')
def contact():
    return render_template('contact.html')  # Should render contact.html

if __name__ == '__main__':
    app.run(debug=True)
    