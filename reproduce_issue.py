from flask import Flask, render_template_string
import os

app = Flask(__name__)

# Mock data
nodes = ["A", "B"]
edges = [{"from": "A", "to": "B"}]

# Read the template file
template_path = os.path.join(os.getcwd(), "graph.html")
with open(template_path, "r") as f:
    template_content = f.read()

@app.route("/")
def index():
    return render_template_string(template_content, nodes=nodes, edges=edges, answer="Test Answer", evidence=[("Chunk 1", 0.95)])

if __name__ == "__main__":
    # Use test_request_context to render without running server
    with app.test_request_context():
        try:
            rendered = index()
            print("Render successful!")
            print(rendered)
        except Exception as e:
            print(f"Render failed: {e}")
