from config import Configuration

from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(Configuration)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
