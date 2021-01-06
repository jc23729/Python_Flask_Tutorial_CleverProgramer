from flask import Flask

app= Flask(__name__)

@app.route('/home/<int:id>')
def hello(id):
    return "Hello, " + str(id)

@app.route('/onlyget')
def get_reg():
    return 'You can only get this webpage. '

if __name__ == "__main__":
    app.run(debug=True)
