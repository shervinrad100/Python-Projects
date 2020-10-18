# TODO:
    # 1. fix HTML/CSS 

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# initialise your webapp as a flask application
webapp = Flask(__name__)

# where db is located
webapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # /// --> relative path, //// --> absolute path

#initialise db with settings from app
db = SQLAlchemy(webapp)

# Create table called Todo
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        ''' return a string every time we create a new element '''
        return '<Task %r>' % self.id

db.create_all()

# homepage 
@webapp.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'Error: 500'
            
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('home.html', tasks=tasks)


@webapp.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'Error: 500'
    
    
@webapp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    
    if request.method == "POST":
        task.content = request.form['content']
        
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Error 500'
    else:
        return render_template('update.html', task=task)

# run flask app
if __name__ == '__main__':
    webapp.run(debug=True)















