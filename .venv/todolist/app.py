from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__, template_folder='todolist')

todolist = [{"todo": "test", "done": False}]

@app.route('/')
def index():
    return render_template("index.html", todolist=todolist)

if __name__ == '__main__':
    app.run(debug=True)