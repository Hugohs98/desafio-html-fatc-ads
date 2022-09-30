from flask import Flask, render_template

app = Flask("__Name__")
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config.update(
  TEMPLATES_AUTO_RELOAD = True
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/quem_somos")
def quem_somos():
    return render_template("quemsomos.html")

if __name__ == '__main__':
  app.run(debug=True)

## python -m venv venv && venv\Scripts\activate && python main.py

