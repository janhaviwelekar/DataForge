from flask import Flask, render_template, request
from retrieval import retrieve_chunks
from entity_graph import build_graph
from answer import generate_answer

app = Flask(__name__)

with open("data/lung_cancer.txt") as f:
    documents = f.read().split(".")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form["query"]

        retrieved = retrieve_chunks(query, documents)
        nodes, edges = build_graph(query, retrieved)
        answer = generate_answer(query, retrieved)

        return render_template(
            "graph.html",
            answer=answer,
            evidence=retrieved,
            nodes=nodes,
            edges=edges
        )

    return render_template("graph.html")

if __name__ == "__main__":
    app.run(debug=True)


try:
    nodes, edges = build_graph(query, evidence)
except Exception:
    nodes, edges = [], []

