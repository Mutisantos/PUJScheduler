import sys
import subprocess
reload (sys)
sys.setdefaultencoding("utf-8")


from flask import Flask, render_template,request, send_from_directory

app = Flask(__name__,static_url_path='')

names = ["Estaban", "Federico", "Hernandez"]

@app.route('/')
def hello_world():
    return render_template("index.html", names = names)

@app.route('/login')
def login():
    numbers = ["1", "2", "3"]
    subprocess.call(["python", "matrix-chain.py"])
    #Leer el archivo de texto generado
    #Interpretarlo y enviarlo al template
    return render_template("index2.html",names=names, numbers = numbers)


if __name__ == '__main__':
    app.run()