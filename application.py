from flask import Flask,render_template

app= Flask(__name__,template_folder="templates")

@app.route("/")
def home(name=None):
    return render_template("index.html",name=name)


@app.route("/result")
def results():
    return render_template("results.html")


if __name__=="__main__":
    app.run(debug= True)

