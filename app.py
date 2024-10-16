from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Rota principal
@app.route("/", methods=["GET", "POST"])
def index():
    html_content = ""
    if request.method == "POST":
        html_content = request.form.get("html_code")
        # Salvando a página HTML criada
        with open("static/pages/page.html", "w") as file:
            file.write(html_content)
        return redirect(url_for("preview"))
    
    return render_template("index.html", html_content=html_content)

# Rota para visualizar a página HTML criada
@app.route("/preview")
def preview():
    return render_template("preview.html")

if __name__ == "__main__":
    if not os.path.exists("static/pages"):
        os.makedirs("static/pages")
    app.run(debug=True)
