from flask import Flask,request, render_template

import subprocess
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def get_cmd():
    if request.method == "GET":

        return render_template("email.html")

    if request.method == "POST":
        if request.form.get("email"):
            url = request.form.get("email")
            temp =  str(subprocess.check_output(["curl",url]))+ " has succesfully subscribed to AppSecEngineer"
        return render_template("email.html",data=temp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)

