from flask import Flask, render_template
import nbformat
from nbconvert import HTMLExporter

app = Flask(__name__)

def render_notebook():
    """Function to convert Jupyter Notebook to HTML"""
    with open("m.ipynb",encoding="utf-8") as f:
        notebook_content = nbformat.read(f, as_version=4)
    html_exporter = HTMLExporter()
    (body, resources) = html_exporter.from_notebook_node(notebook_content)
    return body

@app.route("/")
def home():
    notebook_html = render_notebook()
    return f"""
    <html>
        <head>
            <title>Jupyter Notebook Viewer</title>
        </head>
        <body>
            {notebook_html}
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
