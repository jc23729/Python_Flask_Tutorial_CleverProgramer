from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
############
app= Flask(__name__)

#Path were database is stored, and setup of  Real database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)
# CREATE MODELS
# each class variable is considered a piece of data in database
#a database is just like a big table with columns and rows
class BlogPost(db.Model):
    """this id will always be unique, thats why its primary key, 
    title nullable false means the content has to be there, 
    .String(100) or whatever says is limit the number of characters, if you don't put anything then theirs no limit, author is required but if not there use N/a"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content= db.Column(db.Text, nullable=False)
    author= db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#DEFINE A METHOD(kinda like a function) going to print out to screen whenvever we create a new blog posts
    def __repr__(self):
        return 'Blog post' + str(self.id)
    

#we created a list of dictionaries to create a dummy database, dictionaries is how we want to structure our data
# all_posts= [
#     {
#         'title':'Post 1',
#         'content': 'This is the content of post 1. LAlalalala',
#         'author': 'John'
#         },
#         {
#         'title':'Post 2',
#         'content': 'This is the content of post 2. LAlalalala'
#         }
#     ]
#main template 
@app.route('/')
def index():
    return render_template('index.html')

##we crearted a route and now that we have posts= all_posts(which is linked to our database)
# we will now have access to variable posts that we can use in our html
#for post.html file, so for posts in post, we created a for loop for posts in posts, {{lets ups pull from post.title because post=all posts in our variable we created in app.py in our route}}

@app.route('/posts', methods =['GET', 'POST'])
def posts():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title=post_title, content=post_content, author= post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('posts.html', posts = all_posts)

##Delete posts
@app.route('/posts/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')
##Edit Posts
@app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        post = BlogPost.query.get_or_404(id)
        post.title = request.form['title']
        post.author = request.form['author']
        post.content = request.form['content']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('edit.html')




# @app.route('/home/<int:id>')
# def hello(id):
#     return "Hello, " + str(id)

#route that only gets get requests 
# @app.route('/onlyget', methods=['Get'])
# def get_reg():
#     return 'You can only get this webpage. '

# # if __name__ == "__main__":
# #     app.run(debug=True)
