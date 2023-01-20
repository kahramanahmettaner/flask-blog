from flask import Flask, render_template, url_for
app = Flask(__name__)


posts = [
    {
        'author': 'Taner',
        'title': 'Almanca Ögren',
        'content': 'Artikeller',
        'date_posted': 'Januar 20, 2023'
    },
    {
        'author': 'Batuhan',
        'title': 'NFT ile Para Kazan',
        'content': 'NFT Nedir?',
        'date_posted': 'Januar 21, 2023'
    },
    {
        'author': 'Kadir',
        'title': 'Futbol hakkinda',
        'content': 'Messi bu neyin nes',
        'date_posted': 'Januar 21, 2023'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")


if __name__ == "__main__":
    app.run(debug=True)
