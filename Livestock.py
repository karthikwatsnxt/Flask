## Livestock.py
from flask import Flask, render_template, url_for, flash, redirect, request 
from forms import RegistrationForm, LoginForm, StockForm
from yahoo_fin import stock_info as si

app = Flask(__name__)

app.config['SECRET_KEY'] = '61f56a1aa9a352d93972b27038d6d143'
posts = [
    {
        'stock' : 'TSLA',
        'title' : 'Tesla'
    },
    {
        'stock' : 'AMZN',
        'title' : 'Amazon'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@kk.com' and form.password.data == 'password':
            flash('You have been logged!','success')
            return redirect(url_for('stockform'))
        else:
            flash('Login Unsuccessful. Please check username & password', 'danger')

    return render_template('login.html', title='Login', form=form)

@app.route("/output", methods=['GET','POST'])
def output():
    return render_template('output.html', title='Stock Details')

@app.route("/stockform", methods=['GET','POST'])
def stockform():
    form = StockForm(request.form)
    if form.validate_on_submit():
        global output 
        output=si.get_quote_table(form.stockname.data, dict_result = False)
        return output
        
    return render_template('output.html', title='Stock Details',  form=form, output=output)




if __name__=='__main__':
    app.run(debug=True)
