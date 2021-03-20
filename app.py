from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    content = db.Column(db.String(2048), nullable=False)
    author = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init(self, id, title, content, author):
        self.id = id
        self.title = title
        self.content = content
        self.author = author

@app.route('/')
def index():
    blogs = Blog.query.order_by(Blog.created_at).all()
    return render_template('index.html', blogs =  blogs)




@app.route('/delete/<int:id>')
def delete(id):
    blogToDel = Blog.query.get_or_404(id)
    try:
        db.session.delete(blogToDel)
        db.session.commit()
        return redirect('/')
    except:
        return 'error occured'    




@app.route('/blog/<int:id>')
def blog(id):
    blog = Blog.query.one()
    return render_template('blog.html', blog = blog)

