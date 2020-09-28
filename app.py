from datetime import datetime
import os

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from dotenv import load_dotenv
load_dotenv() # Load env vars

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Init authentication
auth = HTTPBasicAuth()
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Const fields
fields = ['url', 'company', 'company_url',
 'location', 'title', 'description', 'how_to_apply', 'company_logo']

# Admins
users = {
    os.environ.get('LOGIN'): generate_password_hash(os.environ.get('PASSWORD')),
}

# Verification function
@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

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

    def __init__(self, *args, **kwargs):
        super(Job, self).__init__(*args, **kwargs)

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
    new_job = Job(
        type=request.form['type'],
        url=request.form['url'],
        company=request.form['company'],
        company_url=request.form['company_url'],
        location=request.form['location'],
        title=request.form['title'],
        description=request.form['description'],
        how_to_apply=request.form['how_to_apply'],
        company_logo=request.form['company_logo'])

    try:
        db.session.add(new_job)
        db.session.commit()
        return job_schema.jsonify(new_job)
    except BaseException:
        return 'There was an error'


# Get All Jobs
@app.route('/job', methods=['GET'])
@auth.login_required
def get_jobs():
    all_jobs = Job.query.all()
    result = jobs_schema.dump(all_jobs)
    return jsonify(result)


# Get Single Job
@app.route('/job/<id>', methods=['GET'])
def get_job(id):
    job = Job.query.get(id)
    return job_schema.jsonify(job)


# Delete Job
@app.route('/job/<id>/delete', methods=['GET'])
@auth.login_required
def delete_job(id):
    job = Job.query.get(id)
    try:
        db.session.delete(job)
        db.session.commit()
        return job_schema.jsonify(job)
    except BaseException:
        return 'There was an error'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['search']
        try:
            job = Job.query.filter(Job.title==title).first()
            return job_schema.jsonify(job)
        except:
            return 'Job with this title was not found'
    return render_template('index.html')


@app.route('/add', methods=['GET'])
@auth.login_required
def add():
    return render_template('add.html', fields=fields)


# Update a Job
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@auth.login_required
def edit(id):
    if request.method == 'POST':
        job = Job.query.get(id)

        job.type = request.form['type']
        job.url = request.form['url']
        job.company = request.form['company']
        job.company_url = request.form['company_url']
        job.location = request.form['location']
        job.title = request.form['title']
        job.description = request.form['description']
        job.how_to_apply = request.form['how_to_apply']
        job.company_logo = request.form['company_logo']

        try:
            db.session.commit()
            return job_schema.jsonify(job)
        except BaseException:
            return 'There was an error'
    try:
        job = Job.query.get(id)
        return render_template('edit.html', job=job, fields=fields)
    except:
        return 'Job has not found'


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
