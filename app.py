from flask import Flask, render_template, url_for
#from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import request, redirect
from mysql import connector
from projects.todolist import *

app = Flask(__name__)

#To add database test.db
#.\env\Scripts\activate
#python
#from app import db
#db.create_all()

#To add Requirements.txt and Procfile
#pip3 install gunicorn
#pip3 freeze > requirements.txt
#echo web: run this thing >Procfile

#App - ToDoList
@app.route('/', methods=['POST', 'GET'])
def index():
    (result,tasks) = index2()
    print(tasks)
    if result == 0:
        return 'There was an issue. Please try again'
    elif result == 1:
        return redirect('/')
    elif result == 2:
        return render_template('index.html', tasks = tasks)

#App - ToDoList
@app.route('/delete/<int:id>')
def delete(id):
    #task_to_delete = Todo.query.get_or_404(id)
    result = delete2(id)
    if result == 0:
        return 'There was an issue while trying to delete the task!'
    elif result == 1:
        return redirect('/')
  
#App - ToDoList
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    (result,task) = update2(id)
    if result == 0:
        return 'There was an issue while trying to update the task. Please try again!'
    elif result == 1:
        return redirect('/')
    elif result == 2:
        return render_template('update.html', task = task)


if __name__ == "__main__":
    app.run(debug=True)