from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app= Flask(__name__)

#Path were database is stored
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite'



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
