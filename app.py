from datetime import datetime
import os

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)


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

    def __init__(
        self,
        type,
        url,
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
        self.company = company
        self.company_url = company_url
        self.location = location
        self.title = title
        self.description = description
        self.how_to_apply = how_to_apply
        self.company_logo = company_logo

    def __repr__(self):
        return f'<Job {self.title}>'


# Job Schema
class JobSchema(ma.Schema):
    class Meta:
        fields = (
            'id', 'type', 'url', 'created_at', 'company',
            'company_url', 'location', 'title', 'description',
            'how_to_apply', 'company_logo'
        )


# Init schema
job_schema = JobSchema()
jobs_schema = JobSchema(many=True)


# Create a Job
@app.route('/job', methods=['POST'])
def add_job():
    type = request.form['type']
    url = request.form['url']
    company = request.form['company']
    company_url = request.form['company_url']
    location = request.form['location']
    title = request.form['title']
    description = request.form['description']
    how_to_apply = request.form['how_to_apply']
    company_logo = request.form['company_logo']

    new_job = Job(
                    type, url, company, company_url, location,
                    title, description, how_to_apply, company_logo
                )

    try:
        db.session.add(new_job)
        db.session.commit()
        return job_schema.jsonify(new_job)
    except:
        return 'There was an error'


# Get All Jobs
@app.route('/job', methods=['GET'])
def get_jobs():
    all_jobs = Job.query.all()
    result = jobs_schema.dump(all_jobs)
    return jsonify(result)


# Get Single Job
@app.route('/job/<id>', methods=['GET'])
def get_job(id):
    job = Job.query.get(id)
    return job_schema.jsonify(job)


# Update a Job
@app.route('/job/<id>', methods=['PUT'])
def update_job(id):
    job = Job.query.get(id)

    type = request.json['type']
    url = request.json['url']
    company = request.json['company']
    company_url = request.json['company_url']
    location = request.json['location']
    title = request.json['title']
    description = request.json['description']
    how_to_apply = request.json['how_to_apply']
    company_logo = request.json['company_logo']

    job.type = type
    job.url = url
    job.company = company
    job.company_url = company_url
    job.location = location
    job.title = title
    job.description = description
    job.how_to_apply = how_to_apply
    job.company_logo = company_logo

    try:
        db.session.commit()
        return job_schema.jsonify(job)
    except:
        return 'There was an error'


# Delete Job
@app.route('/job/<id>', methods=['DELTE'])
def delete_job(id):
    job = Job.query.get(id)
    try:
        db.session.delete(job)
        db.session.commit()
        return job_schema.jsonify(job)
    except:
        return 'There was an error'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET'])
def add():
    return render_template('add.html')


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
