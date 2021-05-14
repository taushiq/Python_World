from flask import render_template
from datetime import datetime
from flask import request, redirect
from mysql import connector

class Todo:
  def __init__(self, id, content, date_created):
    self.id = id
    self.content = content
    self.date_created = date_created


def index2():
    try:
        con = connector.connect(
        user = "5PJ8RGg4yy",
        password = "Y7VsxHDGyN",
        host = "remotemysql.com",
        database = "5PJ8RGg4yy",
        port = "3306"
        )

    except: 
        return (0,'')



    if request.method == 'POST':
        task_content = request.form['content']
        cursor = con.cursor()
        sql = "insert into to_do_list(content, date_created) values (%s, %s)"
        val = (task_content, datetime.now())
        cursor.execute(sql, val)
        con.commit()
        #print(task_content)
        #new_task = Todo(content=task_content)

        try:
            #db.session.add(new_task)
            #db.session.commit()
            return (1,'')
        except:
            return (0,'')

    else:
        
        cursor = con.cursor()
        query = cursor.execute("SELECT * from to_do_list order by date_created")
        results = cursor.fetchall()
        
        tasks = []

        for i in results:
            tasks.append(Todo(i[0], i[1], i[3]))
        #tasks = Todo.query.order_by(Todo.date_created).all()
        
        return (2,tasks)


def delete2(id):
    try:
        con = connector.connect(
        user = "5PJ8RGg4yy",
        password = "Y7VsxHDGyN",
        host = "remotemysql.com",
        database = "5PJ8RGg4yy",
        port = "3306"
        )
        cursor = con.cursor()
        sql = "delete from to_do_list where id = %s"
        val = (id, )
        cursor.execute(sql, val)
        con.commit()
        return 1
    except:
        return 0

def update2(id):
    try: 
        con = connector.connect(
        user = "5PJ8RGg4yy",
        password = "Y7VsxHDGyN",
        host = "remotemysql.com",
        database = "5PJ8RGg4yy",
        port = "3306"
        )
        cursor = con.cursor()
        query = cursor.execute("SELECT * from to_do_list where id = " + str(id) + " order by date_created")
        results = cursor.fetchall()
        print(results)
        tasks = []

        for i in results:
            tasks.append(Todo(i[0], i[1], i[3]))
        task = tasks[0]  
        

    except:
        return (0,'')
    
    
    if request.method == 'POST':
        #task.content = request.form['content']
        
        try: 
            cursor = con.cursor()
            query = cursor.execute("UPDATE to_do_list SET content = '" + request.form['content'] + "' , date_created = '" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "' WHERE id = " + str(id))
            con.commit()
            #db.session.commit()
            return (1,'')
        except:
            return (0,'')
    else:
        return (2,task)

        
