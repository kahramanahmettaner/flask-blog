from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '0e3592e203f53d011f741e4973e1e949'
# to get random characters in python, use 'import secrets; secrets.token_hex(16)'

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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title="Login", form=form)

if __name__ == "__main__":
    app.run(debug=True)
