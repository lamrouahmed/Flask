from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'flaskblog'

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    content = db.Column(db.String(2048), nullable=False)
    author = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin_login.html')

@app.route('/authenticate_admin', methods = ['POST'])
def authenticate_admin():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        # * Login Success
        blogs = Blog.query.order_by(Blog.created_at).all()

        return render_template('admin_index.html', blogs = blogs)
    else:
        # ! Login Unsuccessful
        return render_template('admin_login.html', error = True)

@app.route('/users')
def users():
    blogs = Blog.query.order_by(Blog.created_at).all()
    return render_template('users_index.html', blogs =  blogs)

@app.route('/delete/<int:id>')
def delete(id):
    blogToDel = Blog.query.get(id)
    try:
        db.session.delete(blogToDel)
        db.session.commit()
        blogs = Blog.query.order_by(Blog.created_at).all()
        return render_template('admin_index.html', blogs = blogs)
    except:
        return render_template('404.html')    

@app.route('/blog/<int:id>')
def blog(id):
    blog = Blog.query.get(id)

    if blog == None:
        return render_template('404.html')
    else:
        return render_template('blog.html', blog = blog)

@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    else:       
        title = request.form.get('title')
        author = request.form.get('author')
        content = request.form.get('content')
        blog = Blog(title, content, author)
        db.session.add(blog)
        db.session.commit()
        blogs = Blog.query.order_by(Blog.created_at).all()
        return render_template('admin_index.html', blogs = blogs)


@app.route('/edit/<int:id>', methods = ['GET', 'POST'])
def edit(id):

    blogToEdit = Blog.query.get(id)

    if blogToEdit == None:
        return render_template('404.html')

    if request.method == 'GET':
        return render_template('edit.html', blog = blogToEdit)
    else:
        blogToEdit.title = request.form.get('title')
        blogToEdit.author = request.form.get('author')
        blogToEdit.content = request.form.get('content')
        timeNow = datetime.now()
        blogToEdit.updated_at = timeNow.strftime('%Y-%m-%d %H:%M:%S')
        db.session.commit()
        blogs = Blog.query.order_by(Blog.created_at).all()
        return render_template('admin_index.html', blogs = blogs)

