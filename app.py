from flask import Flask, render_template

app = Flask(__name__)

# Note: Debugging Purposes not good for production
app.debug = True


@app.route('/')
def getIndex():
    return render_template('index.html')

@app.route('/testCamera')
def testCamera():
    return 'Hello'



if __name__ == '__main__':
    app.run()