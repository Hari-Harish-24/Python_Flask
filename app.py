from flask import Flask , request , render_template, session, redirect,g,url_for
import os

app=Flask (__name__)

app.secret_key= os.urandom(24)

@app.route('/', methods =['GET','POST'])
def route():
    if request.method == 'POST':
        session.pop('user',None)

        if request.form['password'] == 'password':
            session['user'] = request.form['username']
            return redirect(url_for('protected'))
        
    return render_template('index.html')

@app.route("/protected")
def protected():
    if g.user:
        return render_template('protected.html', user=session['user'])
    return redirect(url_for('index'))

@app.before_request("")
def before_request():
    g.user = None

    if 'user' in session:
        g.user = session['user']

@app.route('/Customer_login')
def feature():
    return render_template('Customer.html')


@app.route('/dropsession')
def dropsession():
    session.pop('uses',None)
    return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True)
    