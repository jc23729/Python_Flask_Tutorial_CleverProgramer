from flask import Flask, render_template

app= Flask(__name__)

all_posts= [
    {
        'title':'Post 1',
        'content': 'This is the content of post 1. LAlalalala'
        },
        {
        'title':'Post 2',
        'content': 'This is the content of post 2. LAlalalala'
        }
    ]
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/posts')
def posts():
    return render_template('posts.html')

@app.route('/home/<int:id>')
def hello(id):
    return "Hello, " + str(id)

@app.route('/onlyget', methods=['Get'])
def get_reg():
    return 'You can only get this webpage. '

if __name__ == "__main__":
    app.run(debug=True)
