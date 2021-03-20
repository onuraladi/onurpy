from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/ceonu/Masaüstü/crudluyoz - Kopya/todo.db'
db = SQLAlchemy(app)

@app.route("/")
def index():
    todos=Todo.query.all()
    return render_template("index.html",todos=todos)
@app.route("/add",methods=["POST"])
def add():
    name=request.form.get("name")
    surname =request.form.get("surname")
    mail =request.form.get("mail")
    newTodo=Todo(name=name,surname=surname,mail=mail,complete=False)
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("index"))
    
@app.route("/update" , methods = ['POST'])
def update():
    if request.method == 'POST':
        newname = request.form.get("newname")
        oldname = request.form.get("oldname")
        todo = Todo.query.filter_by(name=oldname).first()
        todo.name=newname
        
        
        
    
        db.session.commit()
        return redirect(url_for("index"))

@app.route("/complete/<string:id>")
def complete(id):
    todo = Todo.query.filter_by(id=id).first()
    if(todo.complete==False):
        todo.complete =True
    else:
        todo.complete =False

    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def delete(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))
class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(80))
    surname= db.Column(db.String(80))
    mail =db.Column(db.Text)
    complete = db.Column(db.Boolean)



if __name__ == "__main__":
    app.run(debug=True)