import sys
import subprocess
import os


reload (sys)
sys.setdefaultencoding("utf-8")


from flask import Flask, render_template,request, send_from_directory

app = Flask(__name__,static_url_path='')


LANGAUGE_OPTIONS = [ {"name":"C++/C","value":"1"},{"name":"Java","value":"2" }, {"name":"Python","value":"1"} ]

names = ["Estaban", "Federico", "Hernandez"]

@app.route('/')
def hello_world():
    return render_template("index.html", languages = LANGAUGE_OPTIONS)

@app.route('/execute/',methods=['POST'])
def login():
    numbers = ["1", "2", "3"]

    filename = request.form['filename']
    language = request.form['language']
    command = []
    if(language == "1"):
        command.append("./"+filename)
    elif (language == "2"):
        command.append("java")
        command.append(filename)    
    elif (language == "3"):
        command.append("python")
        command.append(filename)
    print command
    subprocess.call(command)
    #Leer el archivo de texto generado
    #Interpretarlo y enviarlo al template
    return render_template("index2.html",names=names, numbers = numbers, languages = LANGAUGE_OPTIONS)


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.debug=True 
    app.run(port=8080, host="0.0.0.0")
