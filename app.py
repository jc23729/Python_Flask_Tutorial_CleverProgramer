from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app= Flask(__name__)
########STOPPED ON 1 HOUR OF COURSE###############
#Path were database is stored, and setup of  Real database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///post.db'
db = SQLAlchemy(app)
# each class variable is considered a piece of data in database
#a database is just like a big table with columns and rows
class BlogPost(db.Model):
    """this id will always be unique, thats why its primary key, 
    title nullable false means the content has to be there, 
    .String(100) or whatever says in there is the size allowable, author is required but if not there use N/a"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content= db.Column(db.Text, nullable=False)
    author= db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=dateime.utcnow)
#going to print out to screen 
    def __repr__(self):
        return 'Blog post' + str(self.id)
    

#we created a list of dictionaries to create a dummy database
all_posts= [
    {
        'title':'Post 1',
        'content': 'This is the content of post 1. LAlalalala',
        'author': 'John'
        },
        {
        'title':'Post 2',
        'content': 'This is the content of post 2. LAlalalala'
        }
    ]
#main template 
@app.route('/')
def index():
    return render_template('index.html')

##we crearted a route and now that we have posts= all_posts(which is linked to our database)
# we will now have access to variable posts that we can use in our html
#for post.html file, so for posts in post, we created a for loop for posts in posts, {{lets ups pull from post.title because post=all posts in our variable we created in app.py in our route}}

@app.route('/posts')
def posts():
    return render_template('posts.html', posts = all_posts)

@app.route('/home/<int:id>')
def hello(id):
    return "Hello, " + str(id)

#route that only gets get requests 
@app.route('/onlyget', methods=['Get'])
def get_reg():
    return 'You can only get this webpage. '

if __name__ == "__main__":
    app.run(debug=True)
