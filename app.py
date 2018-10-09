from flask import Flask, request, render_template
from search import searchparse

app = Flask(__name__)

class RepoDetail():

    def __init__(self, data):
        self.repo_name = data.get("repo_name")
        self.description = data.get("description")
        self.updated = data.get("updated")

        if not data.get('licensed_by'):
            self.licensed_by = None
        else:
            self.licensed_by = data.get("licensed_by")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        result = searchparse(request.form['search_bar'])

        return render_template('index.html', result=result)
    return render_template('index.html')


@app.route('/detail/')
def detail():
    try:
        data = eval(request.args.get('item', None))
        repo = RepoDetail(data)
    except TypeError:
        repo = None
    return render_template('detail.html', repo=repo)
