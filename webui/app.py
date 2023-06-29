from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.template_folder = "./"
app.static_folder = "./"

MODELS = ["选择模型...", "模型1"]


def api(essay, model):
    return 0


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        model = request.values.get("model")
        essay = request.values.get("essay")
        result = api(essay, model)
        return redirect(url_for("result", result=result))
    return render_template("index.html", models=MODELS)


@app.route("/result", methods=["GET"])
def result():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)
