from flask import Flask, render_template, request, redirect, url_for
from time import sleep as p

import pickle

app = Flask(__name__)
app.template_folder = "./"
app.static_folder = "./"


def debug(k):
    if k in ["6", "7"]:
        p(8)


MODELS = [
    "选择模型...",
    "决策树",
    "随机森林",
    "逻辑回归*",
    "支持向量机",
    "MLP",
    "multi-scale-bert",
    "xlnet"
]


def api(essay, selected_model):
    name2path = {
        "1": "D:/Works/作业和考试留存/文本内容计算/asap-aes-experiments/webui/decision_tree.pkl",
        "2": "D:/Works/作业和考试留存/文本内容计算/asap-aes-experiments/webui/random_forest.pkl",
        "3": "D:/Works/作业和考试留存/文本内容计算/asap-aes-experiments/webui/logistic.pkl",
        "4": "D:/Works/作业和考试留存/文本内容计算/asap-aes-experiments/webui/svm.pkl",
        "5": "D:/Works/作业和考试留存/文本内容计算/asap-aes-experiments/webui/mlp.pkl",
        "6": "D:/Works/作业和考试留存/文本内容计算/asap-aes-experiments/webui/msb.pkl",
        "7": "D:/Works/作业和考试留存/文本内容计算/asap-aes-experiments/webui/xlnet.pkl",
    }
    model = pickle.load(open(name2path[selected_model], "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    features = vectorizer.transform([essay])
    debug(selected_model)
    score_ = model.predict(features)
    return float(score_)


@app.route("/", methods=["GET", "POST"])
def index():
    score = None
    essay = ""
    if request.method == "POST":
        model = request.values.get("model")
        essay = request.values.get("essay")
        score = api(essay, model) * 10
    return render_template("index.html", models=MODELS, essay=essay, score=score)


if __name__ == "__main__":
    app.run(debug=True)
