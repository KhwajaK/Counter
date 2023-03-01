from flask import Flask, render_template, request, session, redirect

app = Flask (__name__)
app.secret_key="passwierd"

@app.route('/')
def index():
    count = session.get("count", 0)
    session["count"] = count + 1
    return render_template("index.html")

@app.route('/destroy_session')
def destroyit():
    session.clear()
    return redirect('/')

@app.route('/plustwo')
def plustwo():
    count = session.get("count", 0)
    session["count"] = count + 2
    return render_template("index.html")

@app.route('/customincrement', methods=['POST'])
def pluscustom():
    session["increment"] = int(request.form["increment"])
    session["count"] += session["increment"]
    print(request.form)
    return redirect("/")

if __name__ == "__main__":
    app.run(port=8000, debug=True)