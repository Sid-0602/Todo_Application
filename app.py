from flask import Flask,render_template,url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


#intialising the app
app = Flask(__name__)

#intialising the Database for project. 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

@app.before_request
def create_tables():
    db.create_all()

#making a database model for the app 
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200),nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)
    
    #this function returns task and it's id that has been created. 
    def __repr(self):
        return '<Task %r>' % self.id
    
    
    
#app rounting: 
@app.route('/home',methods=['POST','GET'])
@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content = task_content)
        
        try: 
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue adding the task!!"
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html',tasks=tasks) #this is rendering the index page.
    
@app.route('/delete/<int:id>')
def delete(id):
    tasks_to_delete = Todo.query.get_or_404(id)
    
    try: 
        db.session.delete(tasks_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting the task!!'
    
@app.route('/update/<int:id>',methods = ['GET','POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/home')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":
    app.run(debug = True)