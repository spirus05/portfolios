from flask import Flask, render_template

App = Flask(__name__)

@App.route('/')
def main():
    return render_template("index.html")

@App.route('/home')
def about():
    return render_template('/home.html')

@App.route('/feature')
def feature():
    return render_template("feature.html")

@App.route('/about')
def abouts():
    return render_template("/about.html")

@App.route('/contact')
def contact():
    return render_template("/contact.html")

@App.route('/product')
def product():
    return render_template("/product.html")

@App.route('/music')
def music():
    return render_template("/music.html")

@App.route('/anime')
def anime():
    return render_template("/anime.html")

if __name__ == '__main__':
    App.run(debug=True)