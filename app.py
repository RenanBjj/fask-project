from flask import Flask, render_template

JOBS = [
  {
    'id':1,
    'title':'Analista de dados',
    'local':'São Paulo',
    'salario': 'R$ 3500,00'
  },
  {
    'id':2,
    'title':'cientista de dados',
    'local':'São Paulo',
    'salario': 'R$ 3500,00'
  }
]

app = Flask(__name__)
@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)