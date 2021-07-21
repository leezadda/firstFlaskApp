from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#creates database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' #relative path vs asbsoulu\te path (4 dashes)
db = SQLAlchemy(app)

#creates database model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True) #id column
    content = db.Column(db.String(200), nullable = False) #content column
    completed = db.Column(db.Integer, default = 0) #idk
    date_created = db.Column(db.DateTime, default = datetime.utcnow) #not for user, we are checking for their input

def __repr__(self): #return string every time we create a new element
    return '<Task %r>' % self.id

#set route in case of 404 error
@app.route('/', methods =['POST', 'GET']) #METHODS can post and get to route (GET was defalut)

def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content = task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There is an issue adding your task lol'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks = tasks)

if (__name__ == "__main__"):
    app.run(debug = True)