from flask import Flask,request, render_template

import subprocess
app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('index.html')
    
@app.route('/' , methods=['POST'])
def my_form_post():
 url= request.form['url']

 return subprocess.call(["curl",url])



if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 3000, debug = True)