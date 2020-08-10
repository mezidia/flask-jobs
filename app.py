from datetime import datetime
import os

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)


# Job Class/Model
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    url = db.Column(db.Text())
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    company = db.Column(db.String(50))
    company_url = db.Column(db.Text())
    location = db.Column(db.String(50))
    title = db.Column(db.String(50))
    description = db.Column(db.String(200))
    how_to_apply = db.Column(db.Text())
    company_logo = db.Column(db.Text())

    def __init__(self,
                type,
                url,
                created_at,
                company,
                company_url,
                location,
                title,
                description,
                how_to_apply,
                company_logo
    ):
        self.type = type
        self.url = url
        self.created_at = created_at
        self.company = company
        self.company_url = company_url
        self.location = location
        self.title = title
        self.description = description
        self.how_to_apply = how_to_apply
        self.company_logo = company_logo


    def __repr__(self):
        return f'<Job {self.title}>'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
