from json import dump, load
from pathlib import Path

from bottle import post, request, route, run, static_file

STATIC = Path(__file__).parent.parent / "static"

DB = Path(__file__).parent.parent / "data.json"
data = []

if DB.exists():
    with DB.open("r") as f:
        data = load(f)


def db_add(response: dict):
    data.append(response)
    with DB.open("w") as f:
        dump(data, f)


@post("/form")
def form():
    db_add(dict(request.forms.items()))
    return static_file("thanks.html", root=STATIC)


@route("/")
def homepage():
    return static_file("form.html", root=STATIC)


if __name__ == "__main__":
    run(host="localhost", port=8225)
