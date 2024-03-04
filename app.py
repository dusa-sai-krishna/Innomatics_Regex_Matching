
from flask import Flask,render_template,url_for,redirect,request
import re
from get_matches import print_matches,validate_email

app = Flask(__name__)

@app.route('/')
def load_home():
    return render_template('home.html',ans=[],count=0)

@app.route('/results',methods=['POST','GET'])
def get_matches():
    if request.method == 'GET':
        return redirect(url_for('load_home'))
    pattern=request.form['pattern']
    text=request.form['string']
    flag,ans=print_matches(text,pattern)
    return render_template('home.html',ans=ans,count=len(ans))

@app.route('/email')
def load_email():
    return render_template('emailValidation.html',status=None)


@app.route('/emailValidation', methods=['GET','POST'])
def email_validation():
    if request.method == 'GET':
        return redirect(url_for('load_home'))
    email=request.form['email']
    status=validate_email(email)
    return render_template('emailValidation.html',status=status)
    

    
    
    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)