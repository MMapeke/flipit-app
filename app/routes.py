from app import app
from flask import render_template, request
from app.models import model, formopener, function

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
    
@app.route('/results', methods = ['GET', 'POST'])
def results():
    userdata = dict(request.form)
    print(userdata)
    word = userdata["word"]
    print(word)
    reversed = function.reverseit(word)
    print(reversed)
    return render_template("results.html", reversed = reversed)
    
    # Store userdata in a variable, cast as a dictionary, access value using dictionary key
    # userdata = request.form
    # word = userdata["word"] 4
     
    #GET gets data from resource, POST sends to another 7
    
    #file.function(parameters) 1
    
    # rendertemplate, first parameter is file name, and file must be in templates 6
    
    # request.form 2
    
    # render_template(html file, variable = value); {{variable}} 8
    
    # @app.route(/nameOfHTMLFILE) 5
    
    # dictionary 3
    
    